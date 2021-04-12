# !/usr/bin/python
import os
import re
import shutil

# Jupiter
src = "/Users/guillaumebertrand/Documents/perso/astro/lastrophoto/planches/"
dest = "assets/images/photos/"
for root, dirs, files in os.walk(src, topdown=False):
   for name in files:
      filename, file_extension = os.path.splitext(name)
      extok = ['.png','.gif','.jpg']
      if file_extension in extok:
          regex = r"j(\d{4})(\d{2})(\d{2})-(\d{2})h(\d{2}).*"
          matches = re.finditer(regex, filename, re.MULTILINE)
          for matchNum, match in enumerate(matches, start=1):
            year = match.group(1)
            month = match.group(2)
            day = match.group(3)
            hour =  match.group(4)
            minute = match.group(5)
            print(name, year,month,day, hour, minute)
            file_path = "content/%s/%s/%s-jupiter.md" % (year, month, day)
            directory = os.path.dirname(file_path)
            if not os.path.exists(directory):
                os.makedirs(directory)
            f= open(file_path,"w+")
            f.write("---\r\n")
            f.write("date: %s-%s-%s\r\n"%(year,month,day))
            f.write("hours: %s-%s\r\n"%(hour,minute))
            f.write("image: photos/%s\r\n"%(name))
            f.write("categories: \r\n")
            f.write("- Photos \r\n")
            f.write("tags: \r\n")
            f.write("- Jupiter \r\n")
            f.write("title: Jupiter\r\n")
            f.write("---\r\n")
            f.close()
            shutil.copyfile("%s/%s"%(root, name), "%s%s" % (dest, name))

# Mars
src = "/Users/guillaumebertrand/Documents/perso/astro/lastrophoto/planches/"
dest = "assets/images/photos/"
for root, dirs, files in os.walk(src, topdown=False):
   for name in files:
      filename, file_extension = os.path.splitext(name)
      extok = ['.png','.gif','.jpg']
      if file_extension in extok:
          regex = r"mars(\d{4})(\d{2})(\d{2})-(\d{2})h(\d{2}).*"
          matches = re.finditer(regex, filename, re.MULTILINE)
          for matchNum, match in enumerate(matches, start=1):
            year = match.group(1)
            month = match.group(2)
            day = match.group(3)
            hour =  match.group(4)
            minute = match.group(5)
            print(name, year,month,day, hour, minute)
            file_path = "content/%s/%s/%s-mars.md" % (year, month, day)
            directory = os.path.dirname(file_path)
            if not os.path.exists(directory):
                os.makedirs(directory)
            f= open(file_path,"w+")
            f.write("---\r\n")
            f.write("date: %s-%s-%s\r\n"%(year,month,day))
            f.write("hours: %s-%s\r\n"%(hour,minute))
            f.write("image: photos/%s\r\n"%(name))
            f.write("categories: \r\n")
            f.write("- Photos \r\n")
            f.write("tags: \r\n")
            f.write("- Mars \r\n")
            f.write("title: Mars\r\n")
            f.write("---\r\n")
            f.close()
            shutil.copyfile("%s/%s"%(root, name), "%s%s" % (dest, name))

# Mars
src = "/Users/guillaumebertrand/Documents/perso/astro/lastrophoto/planches/"
dest = "assets/images/photos/"
for root, dirs, files in os.walk(src, topdown=False):
   for name in files:
      filename, file_extension = os.path.splitext(name)
      extok = ['.png','.gif','.jpg']
      if file_extension in extok:
          regex = r"m(\d{4})(\d{2})(\d{2})-(\d{2})h(\d{2}).*"
          matches = re.finditer(regex, filename, re.MULTILINE)
          for matchNum, match in enumerate(matches, start=1):
            year = match.group(1)
            month = match.group(2)
            day = match.group(3)
            hour =  match.group(4)
            minute = match.group(5)
            print(name, year,month,day, hour, minute)
            file_path = "content/%s/%s/%s-mars.md" % (year, month, day)
            directory = os.path.dirname(file_path)
            if not os.path.exists(directory):
                os.makedirs(directory)
            f= open(file_path,"w+")
            f.write("---\r\n")
            f.write("date: %s-%s-%s\r\n"%(year,month,day))
            f.write("hours: %s-%s\r\n"%(hour,minute))
            f.write("image: photos/%s\r\n"%(name))
            f.write("categories: \r\n")
            f.write("- Photos \r\n")
            f.write("tags: \r\n")
            f.write("- Mars \r\n")
            f.write("title: Mars\r\n")
            f.write("---\r\n")
            f.close()
            shutil.copyfile("%s/%s"%(root, name), "%s%s" % (dest, name))

# Saturne
src = "/Users/guillaumebertrand/Documents/perso/astro/lastrophoto/planches/"
dest = "assets/images/photos/"
for root, dirs, files in os.walk(src, topdown=False):
   for name in files:
      filename, file_extension = os.path.splitext(name)
      extok = ['.png','.gif','.jpg']
      if file_extension in extok:
          regex = r"s(\d{4})(\d{2})(\d{2})-(\d{2})h(\d{2}).*"
          matches = re.finditer(regex, filename, re.MULTILINE)
          for matchNum, match in enumerate(matches, start=1):
            year = match.group(1)
            month = match.group(2)
            day = match.group(3)
            hour =  match.group(4)
            minute = match.group(5)
            print(name, year,month,day, hour, minute)
            file_path = "content/%s/%s/%s-saturn.md" % (year, month, day)
            directory = os.path.dirname(file_path)
            if not os.path.exists(directory):
                os.makedirs(directory)
            f= open(file_path,"w+")
            f.write("---\r\n")
            f.write("date: %s-%s-%s\r\n"%(year,month,day))
            f.write("hours: %s-%s\r\n"%(hour,minute))
            f.write("image: photos/%s\r\n"%(name))
            f.write("categories: \r\n")
            f.write("- Photos \r\n")
            f.write("tags: \r\n")
            f.write("- Saturne \r\n")
            f.write("title: Saturne\r\n")
            f.write("---\r\n")
            f.close()
            shutil.copyfile("%s/%s"%(root, name), "%s%s" % (dest, name))

# unranus
src = "/Users/guillaumebertrand/Documents/perso/astro/lastrophoto/planches/"
dest = "assets/images/photos/"
for root, dirs, files in os.walk(src, topdown=False):
   for name in files:
      filename, file_extension = os.path.splitext(name)
      extok = ['.png','.gif','.jpg']
      if file_extension in extok:
          regex = r"u(\d{4})(\d{2})(\d{2})-(\d{2})h(\d{2}).*"
          matches = re.finditer(regex, filename, re.MULTILINE)
          for matchNum, match in enumerate(matches, start=1):
            year = match.group(1)
            month = match.group(2)
            day = match.group(3)
            hour =  match.group(4)
            minute = match.group(5)
            print(name, year,month,day, hour, minute)
            file_path = "content/%s/%s/%s-uranus.md" % (year, month, day)
            directory = os.path.dirname(file_path)
            if not os.path.exists(directory):
                os.makedirs(directory)
            f= open(file_path,"w+")
            f.write("---\r\n")
            f.write("date: %s-%s-%s\r\n"%(year,month,day))
            f.write("hours: %s-%s\r\n"%(hour,minute))
            f.write("image: photos/%s\r\n"%(name))
            f.write("categories: \r\n")
            f.write("- Photos \r\n")
            f.write("tags: \r\n")
            f.write("- Uranus \r\n")
            f.write("title: Uranus\r\n")
            f.write("---\r\n")
            f.close()
            shutil.copyfile("%s/%s"%(root, name), "%s%s" % (dest, name))

# Venus
src = "/Users/guillaumebertrand/Documents/perso/astro/lastrophoto/planches/"
dest = "assets/images/photos/"
for root, dirs, files in os.walk(src, topdown=False):
   for name in files:
      filename, file_extension = os.path.splitext(name)
      extok = ['.png','.gif','.jpg']
      if file_extension in extok:
          regex = r"v(\d{4})(\d{2})(\d{2})-(\d{2})h(\d{2}).*"
          matches = re.finditer(regex, filename, re.MULTILINE)
          for matchNum, match in enumerate(matches, start=1):
            year = match.group(1)
            month = match.group(2)
            day = match.group(3)
            hour =  match.group(4)
            minute = match.group(5)
            print(name, year,month,day, hour, minute)
            file_path = "content/%s/%s/%s-venus.md" % (year, month, day)
            directory = os.path.dirname(file_path)
            if not os.path.exists(directory):
                os.makedirs(directory)
            f= open(file_path,"w+")
            f.write("---\r\n")
            f.write("date: %s-%s-%s\r\n"%(year,month,day))
            f.write("hours: %s-%s\r\n"%(hour,minute))
            f.write("image: photos/%s\r\n"%(name))
            f.write("categories: \r\n")
            f.write("- Photos \r\n")
            f.write("tags: \r\n")
            f.write("- Venus \r\n")
            f.write("title: Venus\r\n")
            f.write("---\r\n")
            f.close()
            shutil.copyfile("%s/%s"%(root, name), "%s%s" % (dest, name))