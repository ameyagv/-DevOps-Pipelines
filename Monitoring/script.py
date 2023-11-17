import asyncio
import time
import httpx
import paramiko
import sys
import matplotlib.pyplot as plt

async def send_requests(server_url, num_requests):
    async with httpx.AsyncClient() as client:
        start_time = time.time()
        tasks = [client.get(server_url) for _ in range(num_requests)]
        await asyncio.gather(*tasks)
        end_time = time.time()
        avg_response_time = (end_time - start_time) / num_requests * 1000  
        return avg_response_time
    
    

def monitor_remote_resources(server_address, username, password, interval_seconds, cpu_usage, memory_usage, duration_minutes):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(server_address, username=username, password=password)

    start_time = time.time()
    end_time = start_time + (duration_minutes * 60)

    while time.time() <= end_time:
        # Get CPU Usage
        cpu_stdin, cpu_stdout, cpu_stderr = ssh_client.exec_command("top -bn1 | grep 'Cpu(s)' | sed \"s/.*, *\([0-9.]*\)%* id.*/\1/\" | awk '{print 100 - $1'%'}'
")
        cpu_output = cpu_stdout.read().decode().strip()
        print(f"CPU Output: {cpu_output}")

        # Get Memory Usage
        mem_stdin, mem_stdout, mem_stderr = ssh_client.exec_command("free | awk 'FNR == 2 { print $3/$2*100 }'")
        memory_output = mem_stdout.read().decode().strip()
        print(f"Memory Output: {memory_output}")

        if cpu_output and memory_output:
            cpu_percent = float(cpu_output)
            memory_percent = float(memory_output)

            print(f"Server Resources - CPU Usage: {cpu_percent}%  |  Memory Usage: {memory_percent}%")
            cpu_usage.append(cpu_percent)
            memory_usage.append(memory_percent)
        else:
            print("Error: Unable to retrieve CPU or memory information")

        time.sleep(interval_seconds)

    ssh_client.close()

async def main():
    server1_url = "http://" + str(sys.argv[1]) + ":3000"
    server2_url = "http://" + str(sys.argv[2]) + ":3000"
    num_requests = 1000
    monitoring_interval = 5  # seconds
    duration_minutes = 2   # minutes 

    server1_address = str(sys.argv[1])
    server1_username = str(sys.argv[3])
    server1_password = str(sys.argv[4])

    server2_address = str(sys.argv[2])
    server2_username = str(sys.argv[3])
    server2_password = str(sys.argv[4])

    cpu_usage_server1 = []
    memory_usage_server1 = []
    avg_response_time_server1 = await send_requests(server1_url, num_requests)

    cpu_usage_server2 = []
    memory_usage_server2 = []
    avg_response_time_server2 = await send_requests(server2_url, num_requests)

     # Start monitoring resources on remote servers in separate threads
    asyncio.create_task(
        monitor_remote_resources(server1_address, server1_username, server1_password, monitoring_interval,
                                  cpu_usage_server1, memory_usage_server1, duration_minutes)
    )
    asyncio.create_task(
        monitor_remote_resources(server2_address, server2_username, server2_password, monitoring_interval,
                                  cpu_usage_server2, memory_usage_server2, duration_minutes)
    )

    # Plotting the comparison graph
    plt.figure(figsize=(12, 6))

    # CPU Usage Comparison
    plt.subplot(2, 2, 1)
    plt.plot(cpu_usage_server1, label='Server 1')
    plt.plot(cpu_usage_server2, label='Server 2')
    plt.title('CPU Usage Comparison')
    plt.xlabel('Time (5-second intervals)')
    plt.ylabel('CPU Usage (%)')
    plt.legend()

    # Memory Usage Comparison
    plt.subplot(2, 2, 2)
    plt.plot(memory_usage_server1, label='Server 1')
    plt.plot(memory_usage_server2, label='Server 2')
    plt.title('Memory Usage Comparison')
    plt.xlabel('Time (5-second intervals)')
    plt.ylabel('Memory Usage (%)')
    plt.legend()

    # Average Response Time Comparison
    plt.subplot(2, 1, 2)
    plt.bar(['Server 1', 'Server 2'], [avg_response_time_server1, avg_response_time_server2], color=['blue', 'orange'])
    plt.title('Average Response Time Comparison')
    plt.ylabel('Average Response Time (ms)')

    plt.tight_layout()
    plt.savefig('performance_comparison.png') 
    plt.show()

if __name__ == "__main__":
    asyncio.run(main())
