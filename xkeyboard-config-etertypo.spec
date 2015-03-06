Name: xkeyboard-config-etertypo
Version: 1.2
Release: alt1

Summary: Etersoft typographic layout for X11
License: GPL
Group: System/X11

Url: http://kb.etersoft.ru/Типографская_раскладка_Etersoft

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: http://git.etersoft.ru/people/mdevaev/packages/xkeyboard-config-etertypo.git
Source: %name-%version.tar

BuildArchitectures: noarch
BuildRequires: rpm-build-compat

# we use that dir
Requires: xkeyboard-config

%description
Etersoft typographic layout for X11.
Example: setxkbmap -layout "us,ru(winkeys)" -option -option lv3:lwin_switch,grp:caps_toggle,misc:etertypo,grp_led:caps

%prep
%setup

%install
mkdir -p %buildroot%_datadir/X11/xkb/symbols/
mkdir -p %buildroot%_docdir/etertypo/
cp -f etertypo/symbols_etertypo %buildroot%_datadir/X11/xkb/symbols/etertypo
cp -f etertypo/README %buildroot%_docdir/etertypo/
cp -f etertypo/etertypo-layout.png %buildroot%_docdir/etertypo/

%files
%_datadir/X11/xkb/symbols/etertypo
%_docdir/etertypo/

%changelog
* Fri Jan 16 2015 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt1
- rename file to etertypo
- add rouble sign on H key

* Thu Apr 15 2010 Devaev Maxim <mdevaev@etersoft.ru> 1.1-alt3
- Added keyboard scheme and description

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
