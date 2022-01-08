from contact_app.models import Contact

c1 = Contact(name='tony', birthday='1988-01-01', number='133123456799', address='shandong')
c1.save()
# c1.delete()
# c1.address = 'shanghai'
# c1.save()
# c1 = Contact.objects.get(name='rose')
c1 = Contact.objects.get(name='tony')
print " %s %s %s %s" % (c1.name, c1.birthday, c1.number, c1.address)

