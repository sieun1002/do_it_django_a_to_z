from django.db import models

class Post(models.Model):

  #DB col을 생성하는데, model -> titile
  title = models.CharField(max_length=30)

  #DB col을 생성하는데, model -> content
  content = models.TextField()

  head_image = models.ImageField(upload_to = 'blog/images/%Y/%m/%d/', blank=True)
  file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)

  #DB col을 생성하는데, model -> 시간
  #현재 시간을 새로 작성할 때 바로 넣기
  created_at = models.DateTimeField(auto_now_add = True)

  #수정 시간을 업데이트 했을 때, 수정 현재 시간으로 교채
  update_at = models.DateTimeField(auto_now=True)

  #author: 추후 작성 예정 

  def __str__(self):
    return f'[{self.pk}]{self.title}'
  
  def get_absolute_url(self):
    return f'/blog/{self.pk}/'

# Create your models here.
