from time import sleep
import pygame
import random
import threading
from apscheduler.schedulers.background import BackgroundScheduler
from speech_to_text import run_transcription #this imports the Speech to text

scheduler = BackgroundScheduler()

job_dict = {}

def check_for_stop_command(sch = scheduler):
    """ Continuously check for the 'stop' command from the user """
    while True:
        command = run_transcription()
        if "stop" in command or "Stop" in command:
            print("Stopping scheduler...")
            sch.shutdown()  # Gracefully shut down the scheduler
            print("Scheduler shut down complete.")
            break

def play_alarm_sound(name):
    print("Message:", name)

    # Initialize the mixer module only once
    if not pygame.mixer.get_init():
        pygame.mixer.init()

    list_of_sound = [
      ### File path for your sound 
    ]

    file_path = random.choice(list_of_sound)
    sound = pygame.mixer.Sound(file_path)

    sound.play()
    print("Playing sound from:", file_path)

    # Start a separate thread to check for the 'stop' command
    stop_thread = threading.Thread(target=check_for_stop_command)
    stop_thread.start()

    # Keep the script running until the sound finishes playing
    while pygame.mixer.get_busy():
        pygame.time.Clock().tick(10)
    
    # Ensure the stop thread is properly joined
    stop_thread.join()

def delete_alarm(name, sch= scheduler):          
    """Delete an alarm by its name."""
    job_id = job_dict.get(name)
    if job_id:
        sch.remove_job(job_id)
        print(f"Job {job_id} has been removed.")
        # Remove job from dictionary after deletion
        del job_dict[name]
        return f"Job '{name}' has been deleted"
    else:
        print(f"No job found with the name '{name}'.")
        return f"Failed to delete job '{name}', no such job."

def start_scheduler(name, start_time, end_time):
   
    """Schedule a job with a name, start, and end time."""
    if name in job_dict:
        print(f"Job with the name '{name}' already exists.")
        return f"Job with the name '{name}' already exists."
    
    job = scheduler.add_job(play_alarm_sound, 'interval', start_date=start_time, end_date=end_time, args=[name])
    job_id = job.id
    job_dict[name] = job_id
    print(f"Job '{name}' has been scheduled with job ID: {job_id}")

    # Start the scheduler
    scheduler.start()
    print("Scheduler started. Say 'stop' to exit.")

    return scheduler, job_id




if __name__ == "__main__":
    # Start the scheduler
    scheduler = start_scheduler("time to play", "2024-08-29 04:13:00", "2024-08-29 04:13:40")
