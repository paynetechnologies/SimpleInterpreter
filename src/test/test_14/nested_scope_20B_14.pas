program Main;
   var x, y: real;
   
   procedure Alpha(a : integer);
      var y : integer;
   begin
      x := a + x + y;
   end;

    function factorial(n: integer): longint;
    begin
        if n = 0 then
            factorial := 1
        else
            factorial := n * factorial(n - 1);
    end;
    
begin { Main }
end.  { Main }