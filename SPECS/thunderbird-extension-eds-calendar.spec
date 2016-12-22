%define debug_package %{nil}

Name:           thunderbird-extension-eds-calendar
Version:        0.5
Release:        2%{?dist}
Summary:        Thunderbird extension to synchronize calendars with Evolution Data Server

Group:          Applications/Internet
License:        GPLv2
URL:            https://github.com/balbusm/xul-ext-eds-calendar
Source0:        https://github.com/balbusm/xul-ext-eds-calendar/archive/0.5.tar.gz

Requires:       thunderbird

%description
EDS Calendar Integration is a Thunderbird add-on. It synchronizes Evolution Data Server with
Thunderbird calendar. Gnome Date and Time applet uses EDS to show calendar events. Thanks to
this add-on one will get nice system notifications about upcoming events.

%prep
%setup -q -n xul-ext-eds-calendar-%{version}

%build
./build.sh

%install
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/thunderbird/extensions/
cp -p output/xul-ext-eds-calendar.xpi $RPM_BUILD_ROOT/%{_libdir}/thunderbird/extensions/\{e6696d02-466a-11e3-a162-04e36188709b\}.xpi

%files
%defattr(-,root,root,-)
%{_libdir}/thunderbird/extensions/*.xpi

%changelog
* Thu Dec 22 2016 Ricardo Arguello <rarguello@deskosproject.org> - 0.5-2
- Removed BuildArch: noarch

* Sun Dec 18 2016 Ricardo Arguello <rarguello@deskosproject.org> - 0.5-1
- Initial release for DeskOS
