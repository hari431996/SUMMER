import torch
student_pt_model = torch.load("./student.pt")
print(student_pt_model)

teacher_pt_model = torch.load("./teacher.pt")
print(teacher_pt_model)

csi_supervised_model = torch.load("./csi_supervised.pt")
print(csi_supervised_model)