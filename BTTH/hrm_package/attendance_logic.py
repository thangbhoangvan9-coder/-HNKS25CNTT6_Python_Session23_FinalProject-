def clock_in(attendance_book):
    employee_id = input(
        "Nhập mã nhân viên: "
    ).strip()
    for employee in attendance_book:
        if employee["id"] == employee_id:
            print("Lỗi: Mã nhân viên đã tồn tại!")
            return
    employee_name = input(
        "Nhập tên nhân viên: "
    ).strip()

    clock_in_time = input(
        "Nhập giờ vào (HH:MM): "
    ).strip()

    new_employee = {
        "id": employee_id,
        "name": employee_name,
        "times": (clock_in_time, None)
    }

    attendance_book.append(new_employee)
    print(
        f"Thành công: Đã ghi nhận "
        f"{employee_id} chấm công vào lúc "
        f"{clock_in_time}!"
    )


def clock_out(attendance_book):
    employee_id = input(
        "Nhập mã nhân viên: "
    ).strip()

    clock_out_time = input(
        "Nhập giờ ra (HH:MM): "
    ).strip()

    for employee in attendance_book:

        if employee["id"] == employee_id:
            old_clock_in = employee["times"][0]
            employee["times"] = (
                old_clock_in,
                clock_out_time
            )

            print(
                f"Đã cập nhật giờ ra cho "
                f"{employee_id}"
            )
            return
    print("Không tìm thấy nhân viên!")