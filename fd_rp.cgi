#!/usr/bin/perl -wT
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use strict;
use Fcntl qw(:flock :seek);

#SUBJECT ID
if (param('subjID') eq ""){
&dienice("Please go back and make sure you included your subject ID.");
}
my $i = 1;
my $qname = 'q0';
for ($i = 1; $i <= 32; $i++){
$qname = 'q' . $i;
if (param($qname) eq ""){
&dienice2("Please make sure you have answered all the questions.");
}
}



# DEFINE THE VARIABLES
my($sec, $min, $hr, $mday, $mon, $year, $wday, $yday,$isdst)=
localtime(time);
my $longyr=$year+1900;
my $yr2=substr($longyr,2,2);
my $fixmo = $mon +1;

#RECORD RESPONSES
my $outfile = "/usr/lib/cgi-bin/mw_log/risk_preferences.txt";

open(OUT, ">>$outfile") or &dienice("Couldn't open $outfile:$!");
flock(OUT, LOCK_EX); 
seek(OUT, 0, SEEK_END);
printf(OUT "%02d%02d%02d, %02d%02d%02d, ", $fixmo, $mday, $yr2, $hr, $min, $sec ); 
print OUT param('subjID'), ", ";
print OUT param('q1'), ", ";
print OUT param('q2'), ", ";
print OUT param('q3'), ", ";
print OUT param('q4'), ", ";
print OUT param('q5'), ", ";
print OUT param('q6'), ", ";
print OUT param('q7'), ", ";
print OUT param('q8'), ", ";
print OUT param('q9'), ", ";
print OUT param('q10'), ", ";
print OUT param('q11'), ", ";
print OUT param('q12'), ", ";
print OUT param('q13'), ", ";
print OUT param('q14'), ", ";
print OUT param('q15'), ", ";
print OUT param('q16'), ", ";
print OUT param('q17'), ", ";
print OUT param('q18'), ", ";
print OUT param('q19'), ", ";
print OUT param('q20'), ", ";
print OUT param('q21'), ", ";
print OUT param('q22'), ", ";
print OUT param('q23'), ", ";
print OUT param('q24'), ", ";
print OUT param('q25'), ", ";
print OUT param('q26'), ", ";
print OUT param('q27'), ", ";
print OUT param('q28'), ", ";
print OUT param('q29'), ", ";
print OUT param('q30'), ", ";
print OUT param('q31'), ", ";
print OUT param('q32');

print OUT "\n";
close(OUT);

#PRINT A THANKS PAGE
print header;
print start_html("Thank you");

print<<EndHTML;
<h2 style="font-family: helvetica; fontsize: 90%"> Thank you! </h2>
EndHTML

sub dienice {
     my($msg) = @_;
     print header;
     print start_html("Error");
     print h2("Error");
     print $msg;
     print end_html;
     exit;
}
sub dienice2 {
     my($msg) = @_;
     print header;
     print start_html("Error");
     print h2("Error");
     print $msg;
     print end_html;
     exit;
}

