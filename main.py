# Main application - Run this file to test the streaming manager
# This shows how to use the StreamingManager class

from streaming_manager import StreamingManager

def main():
    """Main function - demonstrates how the streaming manager works"""
    
    # Create an instance of the StreamingManager
    manager = StreamingManager()
    
    print("=" * 60)
    print("STREAMING HOUSEHOLD MANAGER - DEMO")
    print("=" * 60)
    
    # 1. Show summary of all households
    print("\n📊 SYSTEM SUMMARY:")
    print("-" * 60)
    summary = manager.get_summary()
    print(f"Total Households: {summary['total_households']}")
    print(f"Active Households: {summary['active_households']}")
    print(f"Active Streams: {summary['total_active_streams']}/{summary['total_capacity']}")
    print(f"Available Slots: {summary['available_slots']}")
    
    # 2. Show status of all households
    print("\n🏠 HOUSEHOLD STATUS:")
    print("-" * 60)
    all_households = manager.get_all_households()
    for household_id, status in all_households.items():
        print(f"\n{status['name']} ({household_id}):")
        print(f"  Users: {', '.join(status['users'])}")
        print(f"  Status: {status['status']}")
        print(f"  Streams: {status['current_streams']}/{status['max_streams']} in use")
        print(f"  Available: {status['streams_available']} slot(s)")
    
    # 3. Start some streams
    print("\n▶️  STARTING STREAMS:")
    print("-" * 60)
    
    result = manager.start_stream("household_1", "Mom", "Netflix Show")
    print(f"Result: {result['message']}")
    
    result = manager.start_stream("household_1", "Dad", "Movie Time")
    print(f"Result: {result['message']}")
    
    # This should fail because max streams reached
    result = manager.start_stream("household_1", "Someone", "Another Show")
    if "error" in result:
        print(f"Result: ❌ {result['error']}")
    
    result = manager.start_stream("household_2", "Son", "Gaming Stream")
    print(f"Result: {result['message']}")
    
    # 4. Show updated status
    print("\n📈 UPDATED HOUSEHOLD STATUS:")
    print("-" * 60)
    all_households = manager.get_all_households()
    for household_id, status in all_households.items():
        print(f"\n{status['name']}:")
        print(f"  Streams: {status['current_streams']}/{status['max_streams']} in use")
        print(f"  Available: {status['streams_available']} slot(s)")
    
    # 5. Check service health
    print("\n🔧 SERVICE HEALTH:")
    print("-" * 60)
    health = manager.check_service_health()
    for service_name, service_info in health.items():
        print(f"{service_name}: {service_info['status'].upper()}")
    
    # 6. Stop a stream
    print("\n⏹️  STOPPING STREAM:")
    print("-" * 60)
    result = manager.stop_stream("household_1")
    print(f"Result: {result['message']}")
    
    # 7. Final summary
    print("\n📊 FINAL SUMMARY:")
    print("-" * 60)
    summary = manager.get_summary()
    print(f"Active Streams: {summary['total_active_streams']}/{summary['total_capacity']}")
    print(f"Available Slots: {summary['available_slots']}")
    
    print("\n" + "=" * 60)
    print("Demo completed!")
    print("=" * 60)

if __name__ == "__main__":
    main()
