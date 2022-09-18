from imported_admin import User, Privileges, Admin

admin = Admin('denis', 'rrapaj', 'moodfew', 'rrapajdenis2006@gmail.com', 'Albania', '069999999')

admin_privileges = ['can remove users',
                    'can use sudo',
                    'can change modules']
admin.privileges.privileges = admin_privileges
admin.privileges.show_privileges()
