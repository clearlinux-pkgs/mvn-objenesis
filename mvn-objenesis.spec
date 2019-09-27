#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-objenesis
Version  : 2.6
Release  : 12
URL      : https://github.com/easymock/objenesis/archive/2.6.tar.gz
Source0  : https://github.com/easymock/objenesis/archive/2.6.tar.gz
Source1  : https://repo.maven.apache.org/maven2/org/objenesis/objenesis-parent/2.1/objenesis-parent-2.1.pom
Source2  : https://repo.maven.apache.org/maven2/org/objenesis/objenesis-parent/2.5.1/objenesis-parent-2.5.1.pom
Source3  : https://repo1.maven.org/maven2/org/objenesis/objenesis-parent/1.2/objenesis-parent-1.2.pom
Source4  : https://repo1.maven.org/maven2/org/objenesis/objenesis-parent/2.2/objenesis-parent-2.2.pom
Source5  : https://repo1.maven.org/maven2/org/objenesis/objenesis-parent/2.4/objenesis-parent-2.4.pom
Source6  : https://repo1.maven.org/maven2/org/objenesis/objenesis-parent/2.6/objenesis-parent-2.6.pom
Source7  : https://repo1.maven.org/maven2/org/objenesis/objenesis-parent/3.0.1/objenesis-parent-3.0.1.pom
Source8  : https://repo1.maven.org/maven2/org/objenesis/objenesis/1.0/objenesis-1.0.jar
Source9  : https://repo1.maven.org/maven2/org/objenesis/objenesis/1.0/objenesis-1.0.pom
Source10  : https://repo1.maven.org/maven2/org/objenesis/objenesis/1.2/objenesis-1.2.jar
Source11  : https://repo1.maven.org/maven2/org/objenesis/objenesis/1.2/objenesis-1.2.pom
Source12  : https://repo1.maven.org/maven2/org/objenesis/objenesis/2.1/objenesis-2.1.jar
Source13  : https://repo1.maven.org/maven2/org/objenesis/objenesis/2.1/objenesis-2.1.pom
Source14  : https://repo1.maven.org/maven2/org/objenesis/objenesis/2.2/objenesis-2.2.jar
Source15  : https://repo1.maven.org/maven2/org/objenesis/objenesis/2.2/objenesis-2.2.pom
Source16  : https://repo1.maven.org/maven2/org/objenesis/objenesis/2.4/objenesis-2.4.jar
Source17  : https://repo1.maven.org/maven2/org/objenesis/objenesis/2.4/objenesis-2.4.pom
Source18  : https://repo1.maven.org/maven2/org/objenesis/objenesis/2.5.1/objenesis-2.5.1.jar
Source19  : https://repo1.maven.org/maven2/org/objenesis/objenesis/2.5.1/objenesis-2.5.1.pom
Source20  : https://repo1.maven.org/maven2/org/objenesis/objenesis/2.6/objenesis-2.6.jar
Source21  : https://repo1.maven.org/maven2/org/objenesis/objenesis/2.6/objenesis-2.6.pom
Source22  : https://repo1.maven.org/maven2/org/objenesis/objenesis/3.0.1/objenesis-3.0.1.jar
Source23  : https://repo1.maven.org/maven2/org/objenesis/objenesis/3.0.1/objenesis-3.0.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 MIT
Requires: mvn-objenesis-data = %{version}-%{release}
Requires: mvn-objenesis-license = %{version}-%{release}
BuildRequires : apache-maven
BuildRequires : buildreq-mvn

%description
# Objenesis
Objenesis is a library dedicated to bypass the constructor when creating an object. On any JVM there is.

%package data
Summary: data components for the mvn-objenesis package.
Group: Data

%description data
data components for the mvn-objenesis package.


%package license
Summary: license components for the mvn-objenesis package.
Group: Default

%description license
license components for the mvn-objenesis package.


%prep
%setup -q -n objenesis-2.6

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-objenesis
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-objenesis/LICENSE.txt
cp website/site/content/license.html %{buildroot}/usr/share/package-licenses/mvn-objenesis/website_site_content_license.html
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/objenesis/objenesis-parent/2.1
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/objenesis/objenesis-parent/2.1/objenesis-parent-2.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/objenesis/objenesis-parent/2.5.1
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/objenesis/objenesis-parent/2.5.1/objenesis-parent-2.5.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/objenesis/objenesis-parent/1.2
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/objenesis/objenesis-parent/1.2/objenesis-parent-1.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/objenesis/objenesis-parent/2.2
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/objenesis/objenesis-parent/2.2/objenesis-parent-2.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/objenesis/objenesis-parent/2.4
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/objenesis/objenesis-parent/2.4/objenesis-parent-2.4.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/objenesis/objenesis-parent/2.6
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/objenesis/objenesis-parent/2.6/objenesis-parent-2.6.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/objenesis/objenesis-parent/3.0.1
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/objenesis/objenesis-parent/3.0.1/objenesis-parent-3.0.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/objenesis/objenesis/1.0
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/objenesis/objenesis/1.0/objenesis-1.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/objenesis/objenesis/1.0
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/objenesis/objenesis/1.0/objenesis-1.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/objenesis/objenesis/1.2
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/org/objenesis/objenesis/1.2/objenesis-1.2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/objenesis/objenesis/1.2
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/org/objenesis/objenesis/1.2/objenesis-1.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/objenesis/objenesis/2.1
cp %{SOURCE12} %{buildroot}/usr/share/java/.m2/repository/org/objenesis/objenesis/2.1/objenesis-2.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/objenesis/objenesis/2.1
cp %{SOURCE13} %{buildroot}/usr/share/java/.m2/repository/org/objenesis/objenesis/2.1/objenesis-2.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/objenesis/objenesis/2.2
cp %{SOURCE14} %{buildroot}/usr/share/java/.m2/repository/org/objenesis/objenesis/2.2/objenesis-2.2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/objenesis/objenesis/2.2
cp %{SOURCE15} %{buildroot}/usr/share/java/.m2/repository/org/objenesis/objenesis/2.2/objenesis-2.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/objenesis/objenesis/2.4
cp %{SOURCE16} %{buildroot}/usr/share/java/.m2/repository/org/objenesis/objenesis/2.4/objenesis-2.4.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/objenesis/objenesis/2.4
cp %{SOURCE17} %{buildroot}/usr/share/java/.m2/repository/org/objenesis/objenesis/2.4/objenesis-2.4.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/objenesis/objenesis/2.5.1
cp %{SOURCE18} %{buildroot}/usr/share/java/.m2/repository/org/objenesis/objenesis/2.5.1/objenesis-2.5.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/objenesis/objenesis/2.5.1
cp %{SOURCE19} %{buildroot}/usr/share/java/.m2/repository/org/objenesis/objenesis/2.5.1/objenesis-2.5.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/objenesis/objenesis/2.6
cp %{SOURCE20} %{buildroot}/usr/share/java/.m2/repository/org/objenesis/objenesis/2.6/objenesis-2.6.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/objenesis/objenesis/2.6
cp %{SOURCE21} %{buildroot}/usr/share/java/.m2/repository/org/objenesis/objenesis/2.6/objenesis-2.6.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/objenesis/objenesis/3.0.1
cp %{SOURCE22} %{buildroot}/usr/share/java/.m2/repository/org/objenesis/objenesis/3.0.1/objenesis-3.0.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/objenesis/objenesis/3.0.1
cp %{SOURCE23} %{buildroot}/usr/share/java/.m2/repository/org/objenesis/objenesis/3.0.1/objenesis-3.0.1.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/objenesis/objenesis-parent/1.2/objenesis-parent-1.2.pom
/usr/share/java/.m2/repository/org/objenesis/objenesis-parent/2.1/objenesis-parent-2.1.pom
/usr/share/java/.m2/repository/org/objenesis/objenesis-parent/2.2/objenesis-parent-2.2.pom
/usr/share/java/.m2/repository/org/objenesis/objenesis-parent/2.4/objenesis-parent-2.4.pom
/usr/share/java/.m2/repository/org/objenesis/objenesis-parent/2.5.1/objenesis-parent-2.5.1.pom
/usr/share/java/.m2/repository/org/objenesis/objenesis-parent/2.6/objenesis-parent-2.6.pom
/usr/share/java/.m2/repository/org/objenesis/objenesis-parent/3.0.1/objenesis-parent-3.0.1.pom
/usr/share/java/.m2/repository/org/objenesis/objenesis/1.0/objenesis-1.0.jar
/usr/share/java/.m2/repository/org/objenesis/objenesis/1.0/objenesis-1.0.pom
/usr/share/java/.m2/repository/org/objenesis/objenesis/1.2/objenesis-1.2.jar
/usr/share/java/.m2/repository/org/objenesis/objenesis/1.2/objenesis-1.2.pom
/usr/share/java/.m2/repository/org/objenesis/objenesis/2.1/objenesis-2.1.jar
/usr/share/java/.m2/repository/org/objenesis/objenesis/2.1/objenesis-2.1.pom
/usr/share/java/.m2/repository/org/objenesis/objenesis/2.2/objenesis-2.2.jar
/usr/share/java/.m2/repository/org/objenesis/objenesis/2.2/objenesis-2.2.pom
/usr/share/java/.m2/repository/org/objenesis/objenesis/2.4/objenesis-2.4.jar
/usr/share/java/.m2/repository/org/objenesis/objenesis/2.4/objenesis-2.4.pom
/usr/share/java/.m2/repository/org/objenesis/objenesis/2.5.1/objenesis-2.5.1.jar
/usr/share/java/.m2/repository/org/objenesis/objenesis/2.5.1/objenesis-2.5.1.pom
/usr/share/java/.m2/repository/org/objenesis/objenesis/2.6/objenesis-2.6.jar
/usr/share/java/.m2/repository/org/objenesis/objenesis/2.6/objenesis-2.6.pom
/usr/share/java/.m2/repository/org/objenesis/objenesis/3.0.1/objenesis-3.0.1.jar
/usr/share/java/.m2/repository/org/objenesis/objenesis/3.0.1/objenesis-3.0.1.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-objenesis/LICENSE.txt
/usr/share/package-licenses/mvn-objenesis/website_site_content_license.html
