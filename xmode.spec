Name:    xmode
Summary: X Window System (TM) and frame buffer modeline generator
Version: 1.0
Release: %mkrel 6
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
