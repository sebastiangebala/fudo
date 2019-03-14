import os
import random

from PIL import Image
from django.conf import settings
from django.http import HttpResponse

from django.shortcuts import render

from django.core.urlresolvers import resolve
from django.views.decorators.cache import cache_page

from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator

from dummy_images.models import DummyImage


class ImageView(TemplateView):

	template_name = "image.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
        #get url path and extract img width and height
		url_path = self.request.get_full_path()[8:-1].split('x')
		w_image = int(url_path[0])
		h_image = int(url_path[1])

		directory = '../src/dummy_images/img/'
		images_all = os.listdir(directory)

		#as we saving resized images in the same directory we need to skip those before resize
		orginal_img = []
		for i in images_all:
			if i[:7] == 'resized':
				pass
			else:
				orginal_img.append(i)

		single_img = random.choice(orginal_img)
		base_path = settings.MEDIA_ROOT + '/' + single_img
		image = Image.open(base_path)
		image.thumbnail((w_image, h_image))
		new_img_name = '/resized_' + str(w_image) + 'x' + str(h_image) + '_' + single_img
		image.save(settings.MEDIA_ROOT + new_img_name)

		context['image'] = settings.MEDIA_URL + new_img_name
		return context
