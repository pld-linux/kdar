Summary:	KDar - K Disk archiver
Summary(pl.UTF-8):	KDar - archiwizer dysków K
Name:		kdar
Version:	2.1.0
Release:	1
License:	GPL v2
Group:		Applications/Archiving
Source0:	http://dl.sourceforge.net/kdar/%{name}-%{version}.tar.bz2
# Source0-md5:	7f52fb578ad1fa1fc14d80d34f91e2f2
Source1:	%{name}.desktop
URL:		http://kdar.sourceforge.net/
BuildRequires:	dar-devel >= 2.2.1
BuildRequires:	gettext-tools
BuildRequires:	kdelibs-devel >= 9:3.3
BuildRequires:	rpmbuild(macros) >= 1.167
Suggests:	gamin
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
K Disk archiver (KDar) is a KDE GUI-based backup and archiving
program. Use it to prepare your data for storage on CD-Rs, jazz
drives, floppies, even DVDs. KDar uses the dar library by Denis
Corbin. Features include compression and archive splitting.

%description -l pl.UTF-8
KDar - archiwizer dysków K jest bazowanym na GUI KDE programem do
tworzenia kopii zapasowych i archiwizacji. Można go używać do
przygotowania danych mających się znaleźć na płytach CD-R, napędach
jazz, dyskietkach, czy nawet DVD. KDar wykorzystuje bibliotekę dar
Denisa Corbina. Pozwala na kompresję i podział archiwów.

%prep
%setup -q

%build
export CXXFLAGS="%{rpmcxxflags} -DQT_NO_STL"
%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--enable-mode=64 \
	--enable-largefile \
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}

%{__make} %{?with_verbose:VERBOSE=1}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

# remove unusable files
rm $RPM_BUILD_ROOT%{_datadir}/applnk/Utilities/kdar.desktop
rm $RPM_BUILD_ROOT%{_iconsdir}/locolor/*/apps/kdar.png

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO USAGE
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/%{name}
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/*/*
