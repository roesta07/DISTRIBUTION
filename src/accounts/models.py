from django.db import models
from django.db import models
## imported for code
from django.contrib.auth.models import User,AbstractUser,AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
# Third Party
import uuid

# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extrafields):
        email = self.normalize_email(email)
        user = self.model(email=email,
                          **extrafields
                          )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password=None, **extrafields):
        extrafields.setdefault('is_superuser', True)
        extrafields.setdefault('is_staff', True)
        if extrafields.get('is_superuser') is not True:
            raise ValueError("User must have is_superuser to be True")     
        user = self.create_user(email=email,
                                password=password,
                                **extrafields
                                )
        user.save(using=self.db)
        return user


class MyUser(AbstractBaseUser,PermissionsMixin):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    email = models.EmailField(verbose_name=u'email',max_length=350,
        unique=True,
        help_text=u'Any Email',
        error_messages={'unique': "A user with that email already exists. Try Some Other"})
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    # is_active = models.BooleanField(default=True)
    # is_super user is provided by permission Mixins
    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
# Create your models here.
