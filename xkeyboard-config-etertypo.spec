Name: xkeyboard-config-etertypo
Version: 1.1
Release: alt2

Summary: Etersoft typographic layout for X11
License: GPL
Group: System/X11

Url: http://regolit.com/2006/11/26/xkb-unicode/

Packager: Devaev Maxim <mdevaev@etersoft.ru>

# http://git.etersoft.ru/people/mdevaev/packages/xkeyboard-config-etertypo.git
Source: %name-%version.tar

BuildArchitectures: noarch
BuildRequires: rpm-build-compat

%description
Etersoft typographic layout for X11

%prep
%setup

%install
mkdir -p %buildroot%_datadir/X11/xkb/symbols
mkdir -p %buildroot%_docdir/etertypo
cp -f etertypo/symbols_etertypo %buildroot%_datadir/X11/xkb/symbols/typo
cp -f etertypo/README %buildroot%_docdir/etertypo
cp -f etertypo/etertypo-layout.png %buildroot%_docdir/etertypo

%files
%_datadir/X11/xkb/symbols/typo
%_docdir/etertypo/*

%changelog
* Thu Apr 15 2010 Devaev Maxim <mdevaev@etersoft.ru> 1.1-alt2
- Addad pre-revolution symbols, removed yena, back renamed :-)

* Thu Apr 15 2010 Devaev Maxim <mdevaev@etersoft.ru> 1.1-alt1
- Renamed package to xkeyboard-config-etertypo

* Wed Apr 14 2010 Devaev Maxim <mdevaev@etersoft.ru> 1.0-alt4
- Renamed typo to etertypo

* Wed Apr 14 2010 Devaev Maxim <mdevaev@etersoft.ru> 1.0-alt3
- Scheme file not replaced at updates

* Wed Apr 14 2010 Devaev Maxim <mdevaev@etersoft.ru> 1.0-alt2
- Added README text

* Wed Apr 14 2010 Devaev Maxim <mdevaev@etersoft.ru> 1.0-alt1
- Initial build
