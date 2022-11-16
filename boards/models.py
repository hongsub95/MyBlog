from django.db import models

class Board(models.Model):
    title = models.CharField(max_length=50,verbose_name="제목")
    content = models.TextField(verbose_name="내용")
    tag = models.ManyToManyField("Tag",blank=True,verbose_name="태그")
    writer = models.ForeignKey("users.User",related_name="boards",verbose_name="작성자",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성날짜")  
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정날짜")  
    class Meta:
        verbose_name_plural = "게시판"
    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=30,verbose_name="태그이름")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성날짜")  
    class Meta:
        verbose_name_plural = "태그"
    
    def __str__(self):
        return self.name
