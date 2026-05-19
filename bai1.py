print(" --- EMERGENCY TRIAGE SYSTEM -- ")
heart_rate = int(input("Enter patient's heart rate (bpm): "))

# Hệ thống phân loại ưu tiên
if heart_rate > 120:
  print("Priority: RED - Critical condition! Immediate action required.")
elif heart_rate > 100:
  print("Priority: YELLOW - Abnormal. Monitor closely.")
elif heart_rate > 60:
  print("Priority: BLUE - Bradycardia. Require ultrasound.")
else:
  print("Priority: GREEN - Stable. Please wait in the lobby.")

print("Triage process completed.")

# if elif else luồng thực thi theoo thứ tự trừ trên xuống nếu . theo như code cũ > 100 là yellow nhưng nếu > 120 thì sẽ là red nên phải đặt điều kiện > 120 trước để đảm bảo đúng thứ tự ưu tiên.
