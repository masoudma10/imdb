from django.contrib.auth.models import BaseUserManager



class MyUserManager(BaseUserManager):

    def create_user(self, email,
                    first_name,
                    last_name,
                    phone,
                    password):
        """

        :return:
        """
        if not email:
            raise ValueError('users must have Email')
        if not first_name and last_name:
            raise ValueError('users must have first name and last name')

        if not phone:
            raise ValueError('enter your phone number')

        user = self.model(email=self.normalize_email(email),
                          fname=first_name,
                          lname=last_name, phone=phone)
        user.set_password(password)
        user.save(using=self._db)
        return user




    def create_superuser(self, email,
                         first_name,
                         last_name,
                         phone,
                         password):

        user = self.create_user(email,
                                first_name,
                                last_name,
                                phone,
                                password)
        user.is_admin = True
        user.save(using=self._db)