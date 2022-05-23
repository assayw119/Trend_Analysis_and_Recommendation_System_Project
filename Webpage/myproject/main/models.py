# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Demo(models.Model):
    id = models.AutoField(primary_key=True)
    id_num = models.BigIntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    dong = models.TextField(blank=True, null=True)
    sort_x = models.TextField(blank=True, null=True)
    menu_x = models.TextField(blank=True, null=True)
    naver_review_list = models.TextField(blank=True, null=True)
    img_food = models.TextField(blank=True, null=True)
    img_inner = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    sort_y = models.TextField(blank=True, null=True)
    kakao_review_list = models.TextField(blank=True, null=True)
    total_score = models.FloatField(blank=True, null=True)
    total_review_count = models.BigIntegerField(blank=True, null=True)
    clustering = models.BigIntegerField(blank=True, null=True)
    pos_rev_rate = models.FloatField(db_column='pos_rev_Rate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'demo'
    
    # 결과 페이지에서 첫번째 리뷰만 보여주기
    def review_summary(self):
        if self.naver_review_list:
            if '/' in self.naver_review_list:
                return self.naver_review_list.split('/')[0]
        else:
            return self.naver_review_list

    def cluster_repr(self):
        result = []
        # while len(result) < 5:
        #     for i in range(5):
        #         if self.clustering == i:
        #             result.append(self.img_inner.split(',')[0])
        # return result
        # for i in range(5):
        #     for j in self.clustering:
        #         if j == i:
        #             result.append(self.img_inner.split(',')[0])
        #             break
        # return result
        return self.img_inner.split(',')[0]
    
    def img_summary(self):
        if self.img_inner:
            if ',' in self.img_inner:
                return self.img_inner.split(',')[0]
    


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class MainDemo(models.Model):
    id_num = models.BigIntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    dong = models.TextField(blank=True, null=True)
    sort_x = models.TextField(blank=True, null=True)
    menu_x = models.TextField(blank=True, null=True)
    naver_review_list = models.TextField(blank=True, null=True)
    img_food = models.TextField(blank=True, null=True)
    img_inner = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    sort_y = models.TextField(blank=True, null=True)
    kakao_review_list = models.TextField(blank=True, null=True)
    total_score = models.FloatField(blank=True, null=True)
    total_review_count = models.BigIntegerField(blank=True, null=True)
    clustering = models.BigIntegerField(blank=True, null=True)
    pos_rev_rate = models.FloatField(db_column='pos_rev_Rate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'main_demo'