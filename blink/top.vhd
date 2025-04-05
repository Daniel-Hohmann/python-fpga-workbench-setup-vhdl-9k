library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity top is
    port (
        clk : in std_logic;
        led : out std_logic
    );
end entity;

architecture rtl of top is
    signal counter : unsigned(24 downto 0) := (others => '0');
begin
    process(clk)
    begin
        if rising_edge(clk) then
            counter <= counter + 1;
        end if;
    end process;

    led <= counter(24); -- langsames Blinken bei ~1Hz
end architecture;

