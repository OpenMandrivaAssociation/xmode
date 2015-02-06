Name:    xmode
Summary: X Window System (TM) and frame buffer modeline generator
Version: 1.0
Release: 8
Group:   System/X11
License: GPL
Source:  %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
X Window System (TM) and frame buffer modeline generator. If you don't
know how to use this utility, just run it without any argument and you'll
obtain usage help.

%prep
%setup -q

%build
make

%install
make PREFIX=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/X11R6/bin/xmode


%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.0-7mdv2010.0
+ Revision: 435249
- rebuild

* Mon Aug 04 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0-6mdv2009.0
+ Revision: 262626
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0-5mdv2009.0
+ Revision: 257583
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.0-3mdv2008.1
+ Revision: 136612
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Tue May 08 2007 Funda Wang <fundawang@mandriva.org> 1.0-3mdv2008.0
+ Revision: 25011
- mkrel
- fix rpm group
- Import xmode



* Thu Jun 17 2004 Robert Vojta <robert.vojta@mandrake.org> 1.0-2mdk
- rpmlint errors removed
- fixed xmode ownership to root.root

* Thu Jun 17 2004 Robert Vojta <robert.vojta@mandrake.org> 1.0-1mdk
- initial release, based on the sax2 package from the united linux
