import enum 
class GenderEnum(enum.Enum):
    male= "Nữ"
    female ="Nam"
    other= "Khác"
class RoleEnum(enum.Enum):
    user="user"
    admin="admin"
class SubmissionStatusEnum(enum.Enum):
    Pending="Pending"
    Accepted="Accepted"
    Wrong_Answer="Wrong Answer"
    Time_Limit_Exeeded="Time Limit Exeeded"
    Memory_Limit_Exeeded="Memory Limit Exeeded"
    Runtime_Error="Runtime Error"
    Compilation_Error="Compilation Error"
class DiffycultyEnum(enum.Enum):
    Easy="Dễ"
    Medium="Trung Bình"
    Hard="Khó"