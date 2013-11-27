Name:		ucspi-tcp
Summary:	tcpserver and tcpclient for building TCP client-server apps
Version:	0.88
Release:	0%{?dist}
License:	Public Domain
Group:		System/Servers
URL:		http://cr.yp.to/ucspi-tcp.html
Source:		http://cr.yp.to/ucspi-tcp/%{name}-%{version}.tar.gz
Source1:	http://smarden.org/pape/djb/manpages/%{name}-%{version}-man.tar.gz
Patch0:		ucspi-tcp-04182004.patch
Patch1:		ucspi-tcp-rbltimeout.patch
Patch2:		ucspi-tcp-limits.patch
BuildRequires:	zlib-devel >= 1.2.1
Requires:	zlib >= 1.2.1
Obsoletes:	ucspi-tcp-toaster
Obsoletes:	ucspi-tcp-toaster-doc
BuildRoot:      %{_topdir}/BUILDROOT/%{name}-%{version}-%{release}.%{_arch}

%define debug_package %{nil}

#-------------------------------------------------------------------------------
%description
#-------------------------------------------------------------------------------
Tcpserver and tcpclient are easy-to-use command-line tools for building TCP
client-server applications.

Tcpserver waits for incoming connections  and, for each  connection, runs a
program  of  your  choice.  Your  program  receives  environment  variables
showing the local and remote host names, IP addresses, and port numbers.

Tcpserver offers a concurrency  limit to  protect  you from  running out of
processes and memory.   When you  are handling 40 (by default) simultaneous
connections, tcpserver smoothly defers acceptance of new connections.

Tcpserver   also   provides   TCP  access  control   features,  similar  to
tcp-wrappers/tcpd's hosts.allow but much faster.  It's access control rules
are compiled into a  hashed format  with cdb,  so it  can easily  deal with
thousands of different hosts.

This package  includes  a  recordio  tool  that  monitors all the input and
output of a server.

Tcpclient makes a TCP connection and runs a program of your choice. It sets
up the same environment variables as tcpserver.

This package includes several sample clients built on top of tcpclient:
who@, date@, finger@, http@, tcpcat, and mconnect.

Tcpserver  and tcpclient  conform to  UCSPI, the UNIX Client-Server Program
Interface, using the TCP protocol.  UCSPI  tools are  available for several
different networks.

#-------------------------------------------------------------------------------
%prep
#-------------------------------------------------------------------------------
%setup -q
%patch0 -p0
%patch1 -p0
%patch2 -p1

#-------------------------------------------------------------------------------
%build
#-------------------------------------------------------------------------------
echo "gcc %{optflags}"    >conf-cc
echo "gcc -s %{optflags}" >conf-ld
echo "%{_prefix}"         >conf-home

make

#-------------------------------------------------------------------------------
%install
#-------------------------------------------------------------------------------
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
install -m 755 addcr argv0 date@ delcr finger@ \
               fixcrio http@ mconnect mconnect-io rblsmtpd recordio \
               tcpcat tcpclient tcprules tcprulescheck tcpserver who@ \
      %{buildroot}%{_bindir}

tar xvzf %{SOURCE1}
install -m 644 %{name}-%{version}-man/*.1 %{buildroot}%{_mandir}/man1

#-------------------------------------------------------------------------------
%clean
#-------------------------------------------------------------------------------
rm -rf ../%{name}-%{version}-man \
       %{buildroot}

#-------------------------------------------------------------------------------
%files
#-------------------------------------------------------------------------------
%defattr (-,root,root)
%doc CHANGES README TODO VERSION
%attr(0755,root,root) %{_bindir}/addcr
%attr(0755,root,root) %{_bindir}/argv0
%attr(0755,root,root) %{_bindir}/date@
%attr(0755,root,root) %{_bindir}/delcr
%attr(0755,root,root) %{_bindir}/finger@
%attr(0755,root,root) %{_bindir}/fixcrio
%attr(0755,root,root) %{_bindir}/http@
%attr(0755,root,root) %{_bindir}/mconnect
%attr(0755,root,root) %{_bindir}/mconnect-io
%attr(0755,root,root) %{_bindir}/rblsmtpd
%attr(0755,root,root) %{_bindir}/recordio
%attr(0755,root,root) %{_bindir}/tcpcat
%attr(0755,root,root) %{_bindir}/tcpclient
%attr(0755,root,root) %{_bindir}/tcprules
%attr(0755,root,root) %{_bindir}/tcprulescheck
%attr(0755,root,root) %{_bindir}/tcpserver
%attr(0755,root,root) %{_bindir}/who@

# %attr(0644,root,root) %{_mandir}/man1/tcp-qualify.1*
%attr(0644,root,root) %{_mandir}/man1/addcr.1*
%attr(0644,root,root) %{_mandir}/man1/argv0.1*
%attr(0644,root,root) %{_mandir}/man1/date@.1*
%attr(0644,root,root) %{_mandir}/man1/delcr.1*
%attr(0644,root,root) %{_mandir}/man1/finger@.1*
%attr(0644,root,root) %{_mandir}/man1/fixcrio.1*
%attr(0644,root,root) %{_mandir}/man1/http@.1*
%attr(0644,root,root) %{_mandir}/man1/mconnect.1*
%attr(0644,root,root) %{_mandir}/man1/rblsmtpd.1*
%attr(0644,root,root) %{_mandir}/man1/recordio.1*
%attr(0644,root,root) %{_mandir}/man1/tcpcat.1*
%attr(0644,root,root) %{_mandir}/man1/tcpclient.1*
%attr(0644,root,root) %{_mandir}/man1/tcprules.1*
%attr(0644,root,root) %{_mandir}/man1/tcprulescheck.1*
%attr(0644,root,root) %{_mandir}/man1/tcpserver.1*
%attr(0644,root,root) %{_mandir}/man1/who@.1*

#-------------------------------------------------------------------------------
%changelog
#-------------------------------------------------------------------------------
* Fri Nov 15 2013 Eric Shubert <eric@datamatters.us> 0.88-0.qt
- Migrated to github
- Removed -toaster package designation
- Added CentOS 6 support
- Removed unsupported cruft
* Sun Aug 23 2009 Eric Shubert <ejs@shubes.net> 0.88-1.3.9
- Fixed cleanup to work with async i/o on COS4 with unionfs
* Fri Jun 12 2009 Jake Vickers <jake@qmailtoaster.com> 0.88-1.3.8
- Added Fedora 11 support
- Added Fedora 11 x86_64 support
* Tue Jun 02 2009 Jake Vickers <jake@qmailtoaster.com> 0.88-1.3.8
- Added Mandriva 2009 support
* Wed Apr 22 2009 Jake Vickers <jake@qmailtoaster.com> 0.88-1.3.7
- Added Fedora 9 x86_64 and Fedora 10 x86_64 support
* Fri Feb 13 2009 Jake Vickers <jake@qmailtoaster.com> 0.88-1.3.6
- Added Suse 11.1 support
* Sun Feb 08 2009 Jake Vickers <jake@qmailtoaster.com> 0.88-1.3.6
- Added Fedora 9 and 10 support
* Sat Apr 14 2007 Nick Hemmesch <nick@ndhsoft.com> 0.88-1.3.5
- Add CentOS 5 i386 support
- Add CentOS 5 x86_64 support
* Wed Jan 24 2007 JP van de Plasse <jeanpaul@i-serve.nl> 0.88-1.3.4
- Included tcpserver limit patch from http://linux.voyager.hr/ucspi-tcp/
* Sun Jan 14 2007 JP van de Plasse <jeanpaul@i-serve.nl> 0.88-1.3.3
- Included a patch for rblsmtpd so a overall timeout can be set.
* Wed Nov 01 2006 Erik A. Espinoza <espinoza@forcenetworks.com> 0.88-1.3.2
- Added Fedora Core 6 support
* Mon Jun 05 2006 Nick Hemmesch <nick@ndhsoft.com> 0.88-1.3.1
- Add SuSE 10.1 support
* Sat May 13 2006 Nick Hemmesch <nick@ndhsoft.com> 0.88-1.2.11
- Add Fedora Core 5 support
* Fri Apr 28 2006 Nick Hemmesch <nick@ndhsoft.com> 0.88-1.2.10
- Cleanup spec file - No major changes
* Sun Nov 20 2005 Nick Hemmesch <nick@ndhsoft.com> 0.88-1.2.9
- Add SuSE 10.0 and Mandriva 2006.0 support
* Fri Oct 14 2005 Nick Hemmesch <nick@ndhsoft.com> 0.88-1.2.8
- Add Fedora Core 4 x86_64 support
* Sat Oct 01 2005 Nick Hemmesch <nick@ndhsoft.com> 0.88-1.2.7
- Add CentOS 4 x86_64 support
* Wed Jun 29 2005 Nick Hemmesch <nick@ndhsoft.com> 0.88-1.2.6
- Add Fedora Core 4 support
* Fri Jun 03 2005 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.88-1.2.5
- Gnu/Linux Mandrake 10.0,10.1,10.2 support
* Sun May 22 2005 Nick Hemmesch <nick@ndhsoft.com> 0.88-1.2.4
- Make everyuthing into a single rpm
* Sun Feb 27 2005 Nick Hemmesch <nick@ndhsoft.com> 0.88-1.2.3
- Add Fedora Core 3 support
- Add CentOS 4 support
* Wed Jun 02 2004 Nick Hemmesch <nick@ndhsoft.com> 0.88-1.2.2
- Add Fedora Core 2 support
* Sun Apr 18 2004 Nick Hemmesch <nick@ndhsoft.com> 0.88-1.2.1
- Remove Mysql patch and add ucspi-tcp-toaster-20040123.patch
- This version is required by qmail-toaster-1.03-1.2.1 and higher
* Thu Jan 08 2004 Nick Hemmesch <nick@ndhsoft.com> 0.88-1.0.10
- Fix Trustix 2.0 support
* Sat Dec 27 2003 Nick Hemmesch <nick@ndhsoft.com> 0.88-1.0.9
- Add Fedora Core 1 support
* Tue Nov 25 2003 Nick Hemmesch <nick@ndhsoft.com> 0.88-1.0.8
- Add Trustix 2.0 support
* Thu May 15 2003 Miguel Beccari <miguel.beccari@clikka.com> 0.88-1.0.7
- Clean-ups on SPEC  compilation banner, better gcc detects
- Detect gcc-3.2.3
- Red Hat Linux 9.0 support (nick@ndhsoft.com)
- Gnu/Linux Mandrake 9.2 support
* Wed Apr 02 2003 Miguel Beccari <miguel.beccari@clikka.com> 0.88-1.0.6
- Conectiva Linux 7.0 support
- Clean-ups
- Better dependencies for all distros
* Mon Mar 31 2003 Miguel Beccari <miguel.beccari@clikka.com> 0.88-1.0.5
- Conectiva Linux 7.0 support
* Sun Feb 15 2003 Nick Hemmesch <nick@ndhsoft.com> 0.88-1.0.4
- Support for Red Hat 8.0
* Wed Feb 05 2003 Miguel Beccari <miguel.beccari@clikka.com> 0.88-1.0.3
- Support for Red Hat 8.0 thanks to Andrew.J.Kay
* Sat Feb 01 2003 Miguel Beccari <miguel.beccari@clikka.com> 0.88-1.0.2
- Redo Macros to prepare supporting larger RPM OS.
  We could be able to compile (and use) packages under every RPM based
  distribution: we just need to write right requirements.
* Sat Jan 25 2003 Miguel Beccari <miguel.beccari@clikka.com> 0.88-1.0.1
- Added MDK 9.1 support
- Try to use gcc-3.2.1
- Added very little patch to compile with newest GLIBC
- Support dor new RPM-4.0.4
* Sun Oct 06 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.88-0.9.2
- Little clean-ups
* Sun Sep 29 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.88-0.9.1
- RPM macros to detect Mandrake, RedHat, Trustix are OK again. They are
  very basic but they should work.
- Packages are named with their proper releases and bversion is from now
  part of the rpm release: we will continue upgrading safely.
* Mon Sep 23 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.8.0.88-1
- Rebuilded under 0.8 tree.
- Important comments translated from Italian to English.
- Written rpm rebuilds instruction at the top of the file (in english).
- Clean-ups
* Sun Sep 22 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.7.0.88-3
- Clean-ups on patches
* Thu Aug 29 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.7.0.88-2
- Deleted Mandrake Release Autodetection (creates problems)
* Fri Aug 16 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.7.0.88-1
- New version: 0.7 toaster.
- Clean-ups on compiler detecting (now it works again)
- Better macros to detect Mandrake Release
* Thu Aug 13 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.6.0.88-1
- New version: 0.6 toaster.
* Mon Aug 12 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.5.0.88-1
- Doc package is standalone (someone does not ask for man pages)
- Checks for gcc-3.2 (default compiler from now)
- New version: 0.5 toaster.
* Tue Aug 08 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.4.0.88-1
- Rebuild agains 0.4 toaster
* Thu Aug 06 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.3.0.88-3
- Better dependencies for RedHat
* Tue Jul 30 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.3.0.88-2
- Now packages have got 'no sex': you can rebuild them with command line
  flags for specifics targets that are: RedHat, Trustix, and of course
  Mandrake (that is default)
- Fixed the Makefile patch (now it works again): tnx to Carlo Borelli.
* Sun Jul 28 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.3-0.88.1mdk
- toaster v. 0.3: now it is possible upgrading safely because of 'pversion'
  that is package version and 'version' that is toaster version
* Thu Jul 25 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.2-0.88.1mdk
- toaster v. 0.2
- added files attributes
* Thu Jul 18 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.1-0.88.3mdk
- Added tests for gcc-3.1.1
- Added toaster version (we will need to mantain it too): is vtoaster 0.1
- Very soft clean-ups.
* Thu Jul 11 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.88-2mdk
- Renamed the package in toaster (we are building toaster packages with
  toaster patches).
* Mon Jul 01 2002 Miguel Beccari <miguel.beccari@clikka.com> 0.88-1mdk
- First RPM.
