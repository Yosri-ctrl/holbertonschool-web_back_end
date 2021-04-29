-- show all bands with the Glam rock style                                                           
-- with the duration they are formed                                                          
SELECT
        `band_name`,
        IFNULL(`split`, 2021) - `formed` as `lifespan`
FROM metal_bands
WHERE FIND_IN_SET('Glam rock', style)
ORDER BY `lifespan` DESC;
