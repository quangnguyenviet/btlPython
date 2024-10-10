# from import_export import resources, fields
# from django.contrib.auth.models import User
# from .models import Customer
# import pandas as pd

# class CustomerResource(resources.ModelResource):
#     username = fields.Field(attribute='user__username', column_name='username')
#     first_name = fields.Field(attribute='user__first_name', column_name='first_name')
#     last_name = fields.Field(attribute='user__last_name', column_name='last_name')
#     email = fields.Field(attribute='user__email', column_name='email')
#     phone = fields.Field(attribute='phone', column_name='phone')
#     address = fields.Field(attribute='address', column_name='address')
#     dateOfBirth = fields.Field(attribute='dateOfBirth', column_name='dateOfBirth')
#     gender = fields.Field(attribute='gender', column_name='gender')


#     class Meta:
#         model = Customer
#         fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'address', 'dateOfBirth', 'gender')
#         export_order = ('username', 'first_name', 'last_name', 'email', 'phone', 'address', 'dateOfBirth', 'gender')

#     def before_import_row(self, row, **kwargs):
#         if 'password' in row:
#             raw_password = str(row['password']) if pd.notna(row['password']) else 'default_password'
#             user = User.objects.create_user(
#                 username=row['username'],
#                 first_name=row['first_name'],
#                 last_name=row['last_name'],
#                 email=row['email'],
#                 password=raw_password  
#             )
#             row['user'] = user

#         # Nếu không có trường hình ảnh, bạn có thể gán giá trị mặc định
#         row['userImage'] = 'static/images/userImageDefault.png'
