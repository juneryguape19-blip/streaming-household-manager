# Main application - Run this file to test the streaming manager
# This shows how to use the StreamingManager class

from streaming_manager import StreamingManager


def main():
    """Main function - demonstrates how the streaming manager works"""

    manager = StreamingManager()

    print("=" * 60)
    print("WINDOWS HOUSEHOLD MEDIA MANAGER - DEMO")
    print("=" * 60)

    print("\n📊 SYSTEM SUMMARY:")
    print("-" * 60)
    summary = manager.get_summary()
    print(f"Windows Host: {summary['windows_host']}")
    print(f"Media Root: {summary['media_root']}")
    print(f"Total Households: {summary['total_households']}")
    print(f"Active Households: {summary['active_households']}")
    print(f"Active Providers: {summary['active_providers']}")
    print(f"Plan Categories: {summary['plan_categories']}")
    print(f"Active Streams: {summary['total_active_streams']}/{summary['total_capacity']}")
    print(f"Available Slots: {summary['available_slots']}")

    print("\n🧭 PLAN CATEGORIES:")
    print("-" * 60)
    for plan_id, plan in manager.get_plan_summary().items():
        quality = ", ".join(plan["target_quality"])
        households = ", ".join(plan["households"]) or "None assigned"
        print(f"{plan_id}: {plan['name']}")
        print(f"  Recommended App: {plan['recommended_app']}")
        print(f"  Quality: {quality}")
        print(f"  Primary Provider: {plan['primary_provider']}")
        print(f"  Households: {households}")

    print("\n🏠 HOUSEHOLD STATUS:")
    print("-" * 60)
    all_households = manager.get_all_households()
    for household_id, status in all_households.items():
        plan_name = status["plan_details"].get("name", "Unassigned")
        print(f"\n{status['name']} ({household_id}):")
        print(f"  Users: {', '.join(status['users'])}")
        print(f"  Status: {status['status']}")
        print(f"  Plan: {plan_name}")
        print(f"  Streams: {status['current_streams']}/{status['max_streams']} in use")
        print(f"  Available: {status['streams_available']} slot(s)")
        print(f"  Providers: {', '.join(status['recommended_provider_order'])}")

    print("\n🗂️  PROVIDER HEALTH:")
    print("-" * 60)
    health = manager.check_service_health()
    for provider_id, service_info in health.items():
        print(
            f"{provider_id}: {service_info['status'].upper()} "
            f"({service_info['service_type']}, {service_info['access_method']})"
        )

    print("\n▶️  STARTING STREAMS:")
    print("-" * 60)
    result = manager.start_stream("household_1", "Mom", "Licensed Movie Night")
    print(f"Result: {result['message']} [{result['session_id']}] ({result['plan_category']})")

    result = manager.start_stream(
        "household_1",
        "Dad",
        "Concert Recording",
        preferred_provider="webdav_library",
    )
    print(f"Result: {result['message']} [{result['session_id']}] ({result['plan_category']})")

    result = manager.start_stream("household_1", "Someone", "Another Title")
    if "error" in result:
        print(f"Result: ❌ {result['error']}")

    result = manager.start_stream("household_2", "Son", "Family Archive Episode")
    print(f"Result: {result['message']} [{result['session_id']}] ({result['plan_category']})")

    print("\n📈 UPDATED HOUSEHOLD STATUS:")
    print("-" * 60)
    all_households = manager.get_all_households()
    for household_id, status in all_households.items():
        print(f"\n{status['name']} ({household_id}):")
        print(f"  Streams: {status['current_streams']}/{status['max_streams']} in use")
        print(f"  Sessions: {len(status['current_sessions'])}")

    print("\n⏹️  STOPPING STREAM:")
    print("-" * 60)
    result = manager.stop_stream("household_1")
    print(f"Result: {result['message']}")

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
