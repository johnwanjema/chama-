from django import forms
from .models import Profile,Group
from django.utils.translation import ugettext_lazy as _

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_photo','bio','email')

class CreateChamaForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('groupName', 'paybillNo',
                  'contribution_amnt', 'contribution_interval')
        labels = {'groupName': _('Group Name'),
                  'paybillNo': _('M-Pesa Paybill Number'),
                  'contribution_amnt': _('Contribution Amount'),
                  'contribution_interval': _('Contribution Interval')
                  }
        help_texts = {'groupName': _('e.g Mapato Investment Group'),
                      'paybillNo': _('e.g 568942'),
                      'contribution_amnt': _('Amount member should contribute at a time'),
                      }
