-- 1. Liste o nome e sobrenome de todos os clientes do Brasil.
SELECT firstname, lastname
	FROM Customer
    WHERE country = 'Brazil'
    
-- 2. Mostre os nomes de todas as músicas com duração maior que 5 minutos.
SELECT name
	FROM Track
    WHERE milliseconds > 300000
    
-- 3. Liste o nome das músicas e seus respectivos artistas.
SELECT t.Name as Name_music, a.Name as Artist 
	FROM Track t
    JOIN Album al ON t.AlbumId = al.AlbumId
    JOIN Artist a on al.ArtistId = a.ArtistId

-- 4. Mostre o nome, sobrenome, a data da fatura e o total para todas as faturas (Invoice) do ano de 2009 com nome do cliente.
SELECT firstname, lastname, invoicedate, total
	FROM Invoice i
    JOIN Customer c on i.CustomerId = c.CustomerId
    WHERE invoicedate LIKE '2009%'

-- 5. Mostre o total gasto por país (arredondar utilizando duas casas decimais) e o número de compras, ordenado do maior para o menor.
SELECT billingcountry, SUM(total) as total_gasto, COUNT(invoiceid) as num_compras
	FROM Invoice i
    GROUP BY billingcountry
    ORDER BY 3 DESC

-- 6. Liste os 5 gêneros musicais mais vendidos exibindo a quantidade de vendas e o valor total (arredondar utilizando duas casas decimais).
-- 	  Ordene os resultados pela quantidade de vendas (do menor para o maior).
SELECT g.name as Genre, SUM(il.Quantity) as Quantidade, ROUND(SUM(total), 2) as Total
	FROM Genre g
    JOIN Track t on g.GenreId = t.GenreId
    JOIN InvoiceLine il on T.TrackId = il.TrackId
    JOIN Invoice i on il.InvoiceId = i.InvoiceId
    GROUP BY 1
    ORDER BY 2 DESC
    LIMIT 5

-- 7. Mostre o nome, sobrenome, o país e total gasto (arredondar utilizando duas casas decimais) para os clientes com gasto acima da média.
SELECT firstname, lastname, country, total
	from Invoice i
    JOIN Customer c on i.CustomerId = c.CustomerId
    group by 1
    having total > AVG(total)
    
-- 8. Liste artistas e a quantidade de playlists que têm músicas em mais de 3 playlists diferentes.
SELECT a.Name as Artist, COUNT(p.PlaylistId) as qt_playlists
	FROM Track t
    JOIN Album al on t.AlbumId = al.AlbumId
    JOIN Artist a on al.ArtistId = a.ArtistId
    JOIN PlaylistTrack pt on t.TrackId = pt.TrackId
    join Playlist p on pt.PlaylistId = p.PlaylistId
    GROUP BY 1
    HAVING COUNT(DISTINCT (p.PlaylistId)) > 3
    ORDER BY 2 DESC

-- 9. Mostre os nomes dos artistas que têm álbuns mas nunca venderam músicas.
select DISTINCT(a.Name) as Artist
	FROM Track t
    JOIN Album al on t.AlbumId = al.AlbumId
    JOIN Artist a on al.ArtistId = a.ArtistId
    LEFT JOIN InvoiceLine il on t.TrackId = il.TrackId
    GROUP by 1
    HAVING COUNT(invoiceid) = 0
    
-- 10. Exiba o nome e o sobrenome (contacatenados), o cargo (title) de todos os funcionários e seus respectivos supervisores, ordenando pelo id do funcionário.
SELECT e.firstname || ' ' || e.lastname as Name, e.title, sup.FirstName || ' ' || sup.LastName as Supervisor
	from Employee e
    JOIN Employee sup on e.reportsto = sup.EmployeeId
    ORDER BY e.EmployeeId
    
-- 11. Encontre pares de clientes que compraram músicas do mesmo gênero musical, mostrando seus nomes completos (concatenados), o gênero musical em comum e
--     quantas compras em comum eles têm naquele gênero. Considere apenas pares com mais de 3 compras em comum e evite duplicatas
--     (não mostre Cliente A-Cliente B e Cliente B-Cliente A).
SELECT DISTINCT
      c1.CustomerId as Cliente1_ID,
      c1.FirstName || ' ' || c1.LastName as Cliente1,
      c2.CustomerId as Cliente2_ID,
      c2.FirstName || ' ' || c2.LastName as Cliente2,
      g.Name as GeneroMusical,
      COUNT(*) as ComprasEmComum
    FROM Customer c1
    JOIN Invoice i1 ON c1.CustomerId = i1.CustomerId
    JOIN InvoiceLine il1 ON i1.InvoiceId = il1.InvoiceId
    JOIN Track t1 ON il1.TrackId = t1.TrackId
    JOIN Genre g ON t1.GenreId = g.GenreId
    JOIN Track t2 ON t2.GenreId = g.GenreId
    JOIN InvoiceLine il2 ON t2.TrackId = il2.TrackId
    JOIN Invoice i2 ON il2.InvoiceId = i2.InvoiceId
    JOIN Customer c2 ON i2.CustomerId = c2.CustomerId
    WHERE c1.CustomerId < c2.CustomerId 
    GROUP BY c1.CustomerId, c2.CustomerId, g.GenreId
    HAVING ComprasEmComum > 3
    ORDER BY ComprasEmComum DESC;

-- 12. Encontre os gêneros musicais que não têm vendas, mostrando o nome do gênero e garantindo que tanto o número de vendas quanto o número de clientes apareçam como
--	   zero (em vez de NULL) quando não houver dados. Ordene os resultados pelo nome do gênero.
SELECT

-- 13. Desenvolva uma consulta equivalente sem utilizar a clausula WHERE:
--        SELECT DISTINCT 
--            c.FirstName,
--            c.LastName,
--            i.Total
--        FROM Customer c
--        JOIN Invoice i ON c.CustomerId = i.CustomerId
--        WHERE c.Country = 'USA' 
--        AND i.Total > 15
--        ORDER BY i.Total DESC;
SELECT
