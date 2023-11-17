import asyncio
import time
import httpx
import paramiko
import sys
import matplotlib.pyplot as plt

async def send_requests(server_url, request_rate):
    async with httpx.AsyncClient() as client:
       async with httpx.AsyncClient() as client:
        while True:
            await client.get(server_url)
            await asyncio.sleep(1 / request_rate)
    
    

async def monitor_remote_resources(server_address, username, password, interval_seconds, cpu_usage, memory_usage, duration_minutes):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(server_address, username=username, password=password)

    start_time = time.time()
    end_time = start_time + (duration_minutes * 60)

    while time.time() <= end_time:
        # Get CPU Usage
        cpu_stdin, cpu_stdout, cpu_stderr = ssh_client.exec_command("top -bn1 | grep 'Cpu(s)' | sed \"s/.*, *\\([0-9.]*\\)%* id.*/\\1/\" | awk '{print 100 - $1}'")
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
    request_rate = 2         # requests per second
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

    cpu_usage_server2 = []
    memory_usage_server2 = []

    
    send_task1 = asyncio.create_task(send_requests(server1_url, request_rate))
    send_task2 = asyncio.create_task(send_requests(server2_url, request_rate))
    
     # Start monitoring resources on remote servers in separate threads
    monitor_task1 = asyncio.create_task(
        monitor_remote_resources(server1_address, server1_username, server1_password, monitoring_interval,
                                  cpu_usage_server1, memory_usage_server1, duration_minutes)
    )
    monitor_task2 = asyncio.create_task(
        monitor_remote_resources(server2_address, server2_username, server2_password, monitoring_interval,
                                  cpu_usage_server2, memory_usage_server2, duration_minutes)
    )

    await asyncio.gather(monitor_task1, monitor_task2)

    send_task1.cancel()
    send_task2.cancel()
    
    # Plotting the comparison graph
    plt.figure(figsize=(12, 6))

    # CPU Usage Comparison
    plt.subplot(2, 2, 1)
    plt.plot(cpu_usage_server1, label=server1_address)
    plt.plot(cpu_usage_server2, label=server2_address)
    plt.title('CPU Usage Comparison')
    plt.xlabel(f'Time ({monitoring_interval}-second intervals)')
    plt.ylabel('CPU Usage (%)')
    plt.legend()

    # Memory Usage Comparison
    plt.subplot(2, 2, 2)
    plt.plot(memory_usage_server1, label=server1_address)
    plt.plot(memory_usage_server2, label=server2_address)
    plt.title('Memory Usage Comparison')
    plt.xlabel(f'Time ({monitoring_interval}-second intervals)')
    plt.ylabel('Memory Usage (%)')
    plt.legend()

    
    plt.tight_layout()
    plt.savefig('performance_comparison.png') 
    plt.show()

if __name__ == "__main__":
    asyncio.run(main())
