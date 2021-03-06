from django.db import models
from django.utils.html import format_html

from myapi.model.base import Image, Creation


class Category(Creation):
    """分类表 不同分类便于分类搜索"""
    title = models.CharField(max_length=30, unique=True,
                             verbose_name='标题', help_text='标题')

    def __str__(self):
        return self.title

    # def img_display(self):
    #     img1 = ''
    #     if self.img:
    #         img1 = self.img.url
    #     return format_html(
    #         '<img src="{}" width="30px"></img>',
    #         img1,
    #     )

    # img_display.short_description = u'图片'

    class Meta:
        verbose_name = '分类表'
        verbose_name_plural = verbose_name


class Tag(Creation):
    """标签表 可以添加 便于查看"""
    title = models.CharField(max_length=30, unique=True,
                             verbose_name='标题', help_text='标题')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '标签表'
        verbose_name_plural = verbose_name


class Commodity(Creation):
    SELLING_STATUS = (
        (0, '售空'),
        (1, '出售中'),
        (2, '补货中'),
    )
    title = models.CharField(max_length=30, default='',
                             verbose_name='标题', help_text='标题')
    sub_title = models.CharField(max_length=50, blank=True, default='',
                                 verbose_name='子标题', help_text='子标题')
    price = models.FloatField(verbose_name='价格', help_text='价格', default=0.00)
    status = models.PositiveSmallIntegerField(choices=SELLING_STATUS, default=1)
    qr_code = models.CharField(max_length=20, blank=True, default='',
                               verbose_name='二维码', help_text='二维码标签上的信息如果有的话')
    images = models.ManyToManyField(Image, blank=True,
                                    verbose_name='图片', help_text='图片信息')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, blank=True, null=True,
                                 verbose_name='分类', help_text='分类信息')
    tag = models.ManyToManyField(Tag, blank=True,
                                 verbose_name='标签', help_text='标签')
    desc = models.CharField(max_length=100, blank=True, default='',
                            verbose_name='描述', help_text='描述信息')

    def img_display(self):
        return ''

    def __str__(self):
        return self.title + self.sub_title

    img_display.short_description = u'图片'

    class Meta:
        verbose_name = '商品表'
        verbose_name_plural = verbose_name



