%define name icoutils
%define version 0.16.0
%define release 1mdk

Summary: Extract and convert bitmaps from Windows icon and cursor files.
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: Graphics
BuildRoot: %{_tmppath}/%{name}-buildroot
Prefix: %{_prefix}
URL: http://www.student.lu.se/~nbi98oli/
Requires: perl

%description
The icoutils are a set of program for extracting and converting
bitmaps from Microsoft Windows icon and cursor files. These files
usually have the extension .ico or .cur, but they can also be
embedded in executables and libraries (.dll-files). (Such embedded
files are referred to as resources.)

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
cp extresso/extresso extresso/genresscript %buildroot/%_bindir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README AUTHORS ChangeLog NEWS TODO doc/*html doc/*.txt
%_bindir/*
%_mandir/man1/*
%changelog
* Mon Jul  8 2002 Götz Waschk <waschk@linux-mandrake.com> 0.16.0-1mdk
- new version

* Tue Jun  4 2002 Götz Waschk <waschk@linux-mandrake.com> 0.15.0-1mdk
- add man pages
- remove examples from file list
- new version
- autoconf 2.5 macro

* Tue Jan 22 2002 Götz Waschk <waschk@linux-mandrake.com> 0.13.0-1mdk
- initial package
