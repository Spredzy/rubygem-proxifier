%global gem_name proxifier 

Name: rubygem-%{gem_name}		
Version:	
Release:	1%{?dist}
Summary:	

Group:		
License:	
URL:		
Source0:	

BuildRequires:	
Requires:	

%description


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
%make_install


%files
%doc



%changelog

