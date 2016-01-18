#!/bin/bash
gradle_site_url="https://services.gradle.org/distributions"
gradle_site_url_for_download="https://services.gradle.org"
gradle_install_dir=~/develop
gradle_sym_link=gradle

latest_gradle_html=$(curl ${gradle_site_url} 2>/dev/null| egrep "<a href=\"/distributions/gradle-[^\-]+-all.zip\">"|head -n 1)
current_gradle_dir=$(readlink -f ${gradle_install_dir}/${gradle_sym_link})
latest_version=$(echo $latest_gradle_html|egrep -o "\-[0-9\.]+\-"|tr -d '-')
current_version=$(echo $current_gradle_dir|egrep -o "\-[0-9\.]+"|tr -d '-')
if [[ "$latest_version" != "$current_version" ]]; then
	echo need to update gradle to version $latest_version
	gradle_link=$(echo $latest_gradle_html|grep -o "\".*\""|tr -d '"')
	full_url=${gradle_site_url_for_download}/${gradle_link}
	pushd .
	cd ${gradle_install_dir}
	wget $full_url -O gradle.zip
	unzip gradle.zip
	rm gradle.zip
	rm ${gradle_sym_link}
	ln -s "gradle-${latest_version}" gradle
fi
