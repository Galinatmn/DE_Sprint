char s[20] = ""
int t = n/1000
for(i=0; i<t; i++) strcat(s, "M")
m = n%1000;
sot = m/100;
if (sot==9) strcat(s, "CM");
else if (sot==4) strcat(s, "CD");
else if (sot<=3)
  for(i=0;i<sot; i++) strcat(s, "C");
else {
  strcat(s, "D");
  for(i=5;i<sot; i++) strcat(s, "C");
}
// и так далее