%include	/usr/lib/rpm/macros.perl
Summary:	Extract and convert bitmaps from Windows icon and cursor files
Summary(pl.UTF-8):	Narzędzie wyciągające i konwertujące bitmapy z windowsowych plików ikon i kursorów
Name:		icoutils
Version:	0.31.0
Release:	1
License:	GPL v3+
Group:		Applications/Graphics
Source0:	http://savannah.nongnu.org/download/icoutils/%{name}-%{version}.tar.bz2
# Source0-md5:	fe12dcfb7796cb6cb4ac9bb0720ae362
URL:		http://www.nongnu.org/icoutils/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1.5
BuildRequires:	gettext-devel >= 0.14.1
BuildRequires:	libpng-devel
BuildRequires:	rpm-perlprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The icoutils are a set of program for extracting and converting
bitmaps from Microsoft Windows icon and cursor files. These files
usually have the extension .ico or .cur, but they can also be embedded
in executables and libraries (.dll-files). (Such embedded files are
referred to as resources.)

%description -l pl.UTF-8
icoutils to zestaw programów do wyciągania i konwertowania bitmap z
plików ikon i kursorów używanych w Microsoft Windows. Te pliki mają
zazwyczaj rozszerzenie .ico lub .cur, ale mogą być wbudowane w pliki
wykonywalne lub biblioteki (pliki .dll) (takie wbudowane pliki są
nazywane zasobami).

%prep
%setup -q

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/extresso
%attr(755,root,root) %{_bindir}/genresscript
%attr(755,root,root) %{_bindir}/icotool
%attr(755,root,root) %{_bindir}/wrestool
%{_mandir}/man1/extresso.1*
%{_mandir}/man1/genresscript.1*
%{_mandir}/man1/icotool.1*
%{_mandir}/man1/wrestool.1*
