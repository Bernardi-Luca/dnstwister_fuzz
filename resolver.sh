for i in $(cat twistOut.txt)
do
  echo $i"-->"$(dig +short $i @8.8.8.8) >> twistOut_resolv
done
