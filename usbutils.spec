Name: usbutils
Version: 0.86
Release: 2%{?dist}
Source:	http://downloads.sourceforge.net/linux-usb/%{name}-%{version}.tar.gz
URL: http://www.linux-usb.org/
License: GPLv2+
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires: hwdata
BuildRequires: autoconf, libtool, libusb-devel >= 0.1.8
Summary: Linux USB utilities
Group: Applications/System
Conflicts: hotplug < 3:2002_01_14-2
Patch0: usbutils-0.86-hwdata.patch

%description 
This package contains utilities for inspecting devices connected to a
USB bus.

%prep
%setup -q
%patch0 -p1
autoreconf

%build
%configure --sbindir=%{_sbindir}
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

# usb.ids is shipped in hwdata; nuke and adjust .pc file
sed -i 's|usbids=/usr/share/usb.ids|usbids=/usr/share/hwdata/usb.ids|' $RPM_BUILD_ROOT%{_datadir}/pkgconfig/usbutils.pc

%files
%defattr(-,root,root,-)
%{_mandir}/*/*
%{_sbindir}/*
%{_bindir}/*
%{_datadir}/pkgconfig/usbutils.pc
%doc AUTHORS COPYING ChangeLog NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Tue Sep 22 2009  Jiri Moskovcak <jmoskovc@redhat.com> 0.86-2
- spec file fixes - package should not own /usr/{bin,sbin} (rhbz#524005)

* Wed Sep 16 2009  Jiri Moskovcak <jmoskovc@redhat.com> 0.86-1
- new version
- spec file fixes as suggested in rhbz#466041 (info@owlriver.com)

* Mon Aug 24 2009 Karsten Hopp <karsten@redhat.com> 0.82-5
- drop ExcludeArch: s390 s390x as we need this package on s390x to be able to build
  p.e. udev without any hacks

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.82-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul  1 2009  Jiri Moskovcak <jmoskovc@rdhat.com> 0.82-3
- added autoconf to fix build in koji

* Wed Jul  1 2009  Jiri Moskovcak <jmoskovc@redhat.com> 0.82-2
- minor fix in Makefile.am to properly find usb.ids from hwdata
- Resolves: #506974

* Fri May 22 2009 David Zeuthen <davidz@redhat.com> 0.82-1
- Update to 0.82

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.73-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 12 2008 Jiri Moskovcak <jmoskovc@redhat.com> 0.73-2
- spec file cleanup

* Thu Jan 17 2008 Jiri Moskovcak <jmoskovc@redhat.com> 0.73-1
- new version 0.73

* Mon Sep 18 2006 Thomas Woerner <twoerner@redhat.com> 0.72-1
- new version 0.72
- videoterminal (vt) patch is now upstream, dropped

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.71-2.1
- rebuild

* Wed Mar 01 2006 Karsten Hopp <karsten@redhat.de> 1.71-2
- add usbutils-0.71-VT.patch to fix warnings about unknown lines
  (#176903)

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.71-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.71-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Tue Dec 13 2005 Thomas Woerner <twoerner@redhat.com> 0.71-1
- new version 0.71

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Apr 15 2005 Thomas Woerner <twoerner@redhat.com> 0.70-1.1
- added fix from Robert Scheck to fix missing BuildRequires for libusb-devel 
 (#155006)

* Thu Apr 14 2005 Thomas Woerner <twoerner@redhat.com> 0.70-1
- new version 0.70

* Thu Jan 20 2005 David Woodhouse <dwmw2@redhat.com> 0.11-6.2
- Don't byteswap parts of device descriptor which kernel already swapped

* Mon Sep 13 2004 Thomas Woerner <twoerner@redhat.com> 0.11-6.1
- added missing BuildRequires for libtool (#132406)

* Wed Sep  1 2004 Thomas Woerner <twoerner@redhat.com> 0.11-6
- added patch from Aurelien Jarno for unknown HID Country Code entries in
  usb.ids (#127415)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue May  4 2004 Bill Nottingham <notting@redhat.com> 0.11-4
- add patch from USB maintainer to fix various brokenness (#115694, <david-b@pacbell.net>)

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jun  3 2003 Jeff Johnson <jbj@redhat.com>
- add explicit epoch's where needed.

* Mon May 19 2003 Bill Nottingham <notting@redhat.com> 0.11-1
- update to 0.11, fixes #90640
- add patch to fix some warnings (#78462, <d.binderman@virgin.net>)

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Fri Nov 29 2002 Tim Powers <timp@redhat.com> 0.9-9
- remove unpackaged files from the buildroot

* Wed Nov 20 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- exclude mainframe

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Mar 21 2002 Trond Eivind Glomsrød <teg@redhat.com> 0.9-5
- Fix conflict check

* Mon Mar 18 2002 Trond Eivind Glomsrød <teg@redhat.com> 0.9-4
- Conflict with older versions of hotplug which contained
  parts of this package (#60615)

* Fri Feb 22 2002 Trond Eivind Glomsrød <teg@redhat.com> 0.9-3
- Rebuild

* Wed Jan 30 2002 Bill Nottingham <notting@redhat.com> 0.9-2
- require hwdata

* Wed Jan 16 2002 Trond Eivind Glomsrød <teg@redhat.com> 0.9-1
- Initial RPM
- make it build on ia64

