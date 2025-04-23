import queue
import time
import uuid
import random

# Create a queue for requests
request_queue = queue.Queue()

def generate_request():
    """Generate a new request and add it to the queue"""
    # Create a unique request ID
    request_id = str(uuid.uuid4())[:8]  # Use first 8 chars of UUID for readability
    
    # Create a request with a random type
    request_types = ["Tech issue", "Incident", "Billing question", "Bad request"]
    request_type = random.choice(request_types)
    
    request = {
        "id": request_id,
        "type": request_type,
        "time": time.strftime("%H:%M:%S")
    }
    
    # Add the request to the queue
    request_queue.put(request)
    print(f"New request generated: ID {request_id}, Type: {request_type}")
    return request

def process_request():
    """Process a request from the queue if available"""
    if not request_queue.empty():
        # Get a request from the queue
        request = request_queue.get()
        
        # Process the request
        print(f"Processing request: ID {request['id']}, Type: {request['type']}, Time: {request['time']}")
        
        # Simulate processing time
        processing_time = random.uniform(0.5, 2.0)
        time.sleep(processing_time)
        
        print(f"Request {request['id']} has been processed (took {processing_time:.2f} seconds)")
        return request
    else:
        print("Queue is empty, no requests to process")
        return None

def main():
    """Main program loop"""
    print("Request Processing System")
    print("Commands: 'g' - generate request, 'p' - process request, 'q' - quit")
    
    while True:
        command = input("Enter command (g/p/q): ").lower()
        
        if command == 'g':
            generate_request()
        elif command == 'p':
            process_request()
        elif command == 'q':
            print("Exiting program")
            break
        else:
            print("Invalid command. Use 'g', 'p', or 'q'")

if __name__ == "__main__":
    main()
