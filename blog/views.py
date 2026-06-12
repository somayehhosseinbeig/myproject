from django.shortcuts import render

# Create your views here.
def blog_view(request):
  return render(request,'blog/blog-home.html')

def blog_single(request):
  context = {'title':'title subject',
  'content':'jhsdgfsdj dskjfhsd fdsjfhfjsd hjdsfhfj fdsjfh',
  'author':'Somayeh Hosseinbeig'}
  return render(request,'blog/blog-single.html',context)