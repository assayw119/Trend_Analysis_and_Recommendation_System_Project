# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from re import A
from django.db import models
import random
from django.contrib.auth.models import User


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


class Data(models.Model):
    id = models.BigIntegerField(primary_key=True)
    # saver = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField(blank=True, null=True)
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
    category = models.BigIntegerField(blank=True, null=True)
    cluster = models.BigIntegerField(blank=True, null=True)
    review_score = models.FloatField(blank=True, null=True)
    region_code = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data'
    
    # 결과 페이지에서 첫번째 리뷰만 보여주기
    def review_summary(self):
        if self.naver_review_list:
            if '/' in self.naver_review_list:
                review = self.naver_review_list.split('/')[0]
                if len(review) > 160:
                    review = review[:160] + "..."
                return review
        else:
            return self.naver_review_list
    
    # 상세 페이지에서 네이버 리뷰 보여주기
    def naver_review(self):
        if self.naver_review_list:
            if '/' in self.naver_review_list:
                return self.naver_review_list.split('/')
        else:
            return ''
    
    # 상세 페이지에서 카카오 리뷰 보여주기
    def kakao_review(self):
        if self.kakao_review_list:
            if '/' in self.kakao_review_list:
                return self.kakao_review_list.split('/')
        else:
            return ''
    
    # 음식점 내부 이미지 반복출력 위해 split 후 리스트로 반환
    def img_summary(self):
        if self.img_inner:
            if ',' in self.img_inner:
                return random.choice(self.img_inner.split(','))

    # 음식점 대표 음식 이미지
    def food_summary(self):
        if self.img_food:
            if ',' in self.img_food:
                return self.img_food.split(',')[0]
    
    # 음식점 음식 이미지 반복출력
    def food_list(self):
        if self.img_food:
            if ',' in self.img_food:
                return self.img_food.split(',')
        else:
            return "../static/assets/img/img_nothing.jpeg"
    
    # 음식점 내부 이미지 반복출력
    def rest_list(self):
        if self.img_inner:
            if ',' in self.img_inner:
                return self.img_inner.split(',')
        else:
            return "../static/assets/img/img_nothing.jpeg"
    
    # total score 100%로 표시
    def total_score_(self):
        return int(self.total_score) * 20


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


class MainData(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
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
    category = models.BigIntegerField(blank=True, null=True)
    cluster = models.BigIntegerField(blank=True, null=True)
    review_score = models.FloatField(blank=True, null=True)
    region_code = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'main_data'