//��������� ����� ���� ������ �������, ��� ��������� �� ��� ����.
//tableID � ������������� �������
//selColor � ���� ��� ��������� ����
//normColor � ������� ���� ����
function trsetcolor(tableID, selColor, normColor){
     table = document.getElementById(tableID);
     var trs=table.getElementsByTagName('tr');
     for(var j=0;j<trs.length;j++){
       trs[j].onmouseover=function(){this.bgColor = selColor;return false;};
       trs[j].onmouseout=function(){this.bgColor = normColor;return false;};
     }
}

function trsetcolor_now(tableID, selColor){
     table = document.getElementById(tableID);
     var trs=table.getElementsByTagName('tr');
     for(var j=0;j<trs.length;j++){
       trs[j].bgColor = selColor; 
     }
}

//trsetcolor('table_stock', '#66ff99', '#ffffff');

