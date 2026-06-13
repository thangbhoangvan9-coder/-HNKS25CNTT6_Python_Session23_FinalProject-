from datetime import datetime


def evaluate_flex_time(attendance_book):
    print("\n--- KẾT QUẢ ĐÁNH GIÁ ---")
    latest_allowed = datetime.strptime(
        "10:00",
        "%H:%M"
    )

    for employee in attendance_book:
        clock_in, clock_out = employee["times"]
        if clock_out is None:
            print(
                f"{employee['id']} - "
                f"Chưa chấm công ra."
            )
            continue
        start_time = datetime.strptime(
            clock_in,
            "%H:%M"
        )
        end_time = datetime.strptime(
            clock_out,
            "%H:%M"
        )

        if start_time > latest_allowed:

            print(
                f"{employee['id']} - "
                f"Vi phạm: Đến muộn quá 90 phút."
            )

            continue

        total_hours = (
            end_time - start_time
        ).total_seconds() / 3600

        if total_hours < 9:
            print(
                f"{employee['id']} - "
                f"Vi phạm: Về sớm, chưa hoàn thành "
                f"đủ 9 tiếng bù giờ."
            )

        else:
            print(
                f"{employee['id']} - "
                f"Hợp lệ: Hoàn thành ca làm việc."
            )