Summary:	Extract and convert bitmaps from Windows icon and cursor files
Summary(pl):	Narz�dzie wyci�gaj�ce i konwertuj�ce bitmapy z windowsowych plik�w ikon i kursor�w
Name:		icoutils
Version:	0.16.0
Release:	2
License:	GPL
Group:		Applications/Graphics
Source0:	http://www.student.lu.se/~nbi98oli/src/%{name}-%{version}.tar.gz
URL:		http://www.student.lu.se/~nbi98oli/
Requires:	perl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The icoutils are a set of program for extracting and converting
bitmaps from Microsoft Windows icon and cursor files. These files
usually have the extension .ico or .cur, but they can also be embedded
in executables and libraries (.dll-files). (Such embedded files are
referred to as resources.)

%description -l pl
icoutils to zestaw program�w do wyci�gania i konwertowania bitmap z
plik�w ikon i kursor�w u�ywanych w Microsoft Windows. Te pliki maj�
zazwyczaj rozszerzenie .ico lub .cur, ale mog� by� wbudowane w pliki
wykonywalne lub biblioteki (pliki .dll) (takie wbudowane pliki s�
nazywane zasobami).

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

install extresso/extresso extresso/genresscript $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS ChangeLog NEWS TODO doc/*html doc/*.txt
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
