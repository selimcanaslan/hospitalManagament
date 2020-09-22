CREATE DATABASE hastane;
use hastane
CREATE TABLE hasta(
hastaId int identity(100,1) PRIMARY KEY,
hasta_ad varchar(20) NOT NULL,
hasta_soyad varchar(20) NOT NULL,
hasta_adres varchar(255) NOT NULL,
hasta_CepTel varchar(10) NOT NULL
	CONSTRAINT ck_hasta_CepTel CHECK(hasta_CepTel LIKE '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'),
hasta_tcno varchar(11) UNIQUE NOT NULL
	CONSTRAINT ck_hasta_tcno CHECK (DATALENGTH(hasta_tcno) = 11),
hasta_cinsiyet char(5) NOT NULL
	CONSTRAINT ck_hasta_cins CHECK(hasta_cinsiyet IN ('ERKEK','KIZ')),
hasta_kayittar date NOT NULL
	CONSTRAINT ck_hasta_kayittar CHECK(hasta_kayittar <= getdate()) DEFAULT(getdate()),
hasta_kanGrubu varchar(10) NOT NULL,
	CONSTRAINT ck_kanGrubu CHECK(hasta_kanGrubu IN ('A+','A-','B+','B-','AB+','AB-','0+','0-')),
hasta_dogTar date NOT NULL
	CONSTRAINT ck_dogTar CHECK (hasta_dogTar <= getdate()),
hasta_dogYer varchar(20) NOT NULL
	CONSTRAINT ck_dogYer CHECK(hasta_DogYer IN ('Adana', 'Adıyaman', 'Afyon', 'Ağrı', 'Amasya', 'Ankara', 'Antalya', 'Artvin','Aydın', 'Balıkesir', 'Bilecik', 'Bingöl', 'Bitlis', 'Bolu', 'Burdur', 'Bursa', 'Çanakkale','Çankırı', 'Çorum', 'Denizli', 'Diyarbakır', 'Edirne', 'Elazığ', 'Erzincan', 'Erzurum', 'Eskişehir','Gaziantep', 'Giresun', 'Gümüşhane', 'Hakkari', 'Hatay', 'Isparta', 'Mersin', 'İstanbul', 'İzmir','Kars','Kastamonu','Kayseri','Kırklareli','Kırşehir','Kocaeli','Konya','Kütahya', 'Malatya','Manisa', 'Kahramanmaraş', 'Mardin', 'Muğla', 'Muş', 'Nevşehir', 'Niğde', 'Ordu', 'Rize', 'Sakarya','Samsun', 'Siirt', 'Sinop', 'Sivas', 'Tekirdağ', 'Tokat', 'Trabzon', 'Tunceli', 'Şanlıurfa', 'Uşak','Van', 'Yozgat', 'Zonguldak', 'Aksaray', 'Bayburt', 'Karaman', 'Kırıkkale', 'Batman', 'Şırnak','Bartın', 'Ardahan', 'Iğdır', 'Yalova', 'Karabük', 'Kilis', 'Osmaniye', 'Düzce')))

CREATE TABLE doktor(
doktorId smallint identity(500,1) PRIMARY KEY,
doc_ad varchar(20) NOT NULL,
doc_soyad varchar (20) NOT NULL,
doc_unvan varchar(20) NOT NULL,
doc_cinsiyet char(5) NOT NULL 
	CONSTRAINT ck_doktor_cins CHECK(doc_cinsiyet IN ('ERKEK','KIZ')),
doc_DogTar date
	CONSTRAINT ck_doktor_dogTar CHECK(doc_DogTar <= getdate()),
)
CREATE TABLE muayene(
muayeneId int identity(300,1) PRIMARY KEY,
hastaId int NOT NULL FOREIGN KEY (hastaId) REFERENCES hasta(hastaId) ON DELETE CASCADE ON UPDATE CASCADE,
muayeneTar date
	CONSTRAINT df_muayeneTar DEFAULT(getdate()),
muayeneSaat time
	CONSTRAINT df_muayeneSaat DEFAULT(getdate()),
doktorId smallint NOT NULL FOREIGN KEY (doktorId) REFERENCES doktor(doktorId) ON DELETE CASCADE ON UPDATE CASCADE,
muayeneTuru varchar(30)
)
CREATE TABLE muayeneSonuc(
muayeneSonucId smallint identity(400,1) PRIMARY KEY,
muayeneId int NOT NULL FOREIGN KEY (muayeneId) REFERENCES muayene(muayeneId) ON DELETE CASCADE ON UPDATE CASCADE,
aciklama varchar(255) NOT NULL,
)
CREATE TABLE ameliyat(
ameliyatId smallint identity(600,1),
ameliyatturu varchar(25) NOT NULL,
ameliyataciklama varchar(255) NOT NULL,
ameliyatucret int NOT NULL,
hastaId int NOT NULL FOREIGN KEY (hastaId) REFERENCES hasta(hastaId) ON DELETE CASCADE ON UPDATE CASCADE,
doktorId smallint FOREIGN KEY (doktorId) REFERENCES doktor(doktorId) ON DELETE CASCADE ON UPDATE CASCADE,
)
CREATE TABLE users(
userId smallint identity(1,1),
username varchar(15) UNIQUE NOT NULL,
pass varchar(20) NOT NULL,
yetki varchar(20) NOT NULL
)
CREATE TABLE silinmis_hasta_kayitlari (
hastaId int,
hasta_ad varchar(20),
hasta_soyad varchar(20),
hasta_adres varchar(255),
hasta_CepTel varchar(10),
hasta_tcno varchar(11),
hasta_cinsiyet char(5),
hasta_kayittar datetime,
hasta_kanGrubu varchar(10),
hasta_dogTar date,
hasta_dogYer varchar(20),
silinme_tarihi date
	CONSTRAINT df_silinme_hasta
	DEFAULT getdate()
)
CREATE TABLE silinmis_doktor_kayitlari(
doktorId smallint,
doktor_ad varchar(20),
doktor_soyad varchar(20),
doktor_unvan varchar(20),
doktor_cinsiyet char(5),
doktor_dogTar date,
silinme_tarihi date
	CONSTRAINT df_silinme_dok
	DEFAULT getdate()
)

CREATE TABLE silinmis_muayene_kayitlari(
muayeneId int,
hastaId int,
muayeneTar date,
MuayeneSaat time,
doktorId smallint,
muayeneTuru varchar(30),
silinme_tarihi date
	CONSTRAINT df_silinme
	DEFAULT getdate()
)


											--INDEXES
CREATE CLUSTERED INDEX ameliyat_index ON dbo.ameliyat(ameliyatId)
CREATE CLUSTERED INDEX users_index ON dbo.users(userId)

											-- STORED PROCEDURES
CREATE PROCEDURE hasta_getir
@tcno varchar(11)
AS
SELECT * FROM hasta WHERE hasta_tcno=@tcno
GO

CREATE PROCEDURE hasta_getir_ad
@ad varchar(25)
AS
SELECT * FROM hasta WHERE hasta_ad=@ad
GO

CREATE PROCEDURE muayene_listele
@hastaId smallint
AS
SELECT * FROM muayene WHERE hastaId=@hastaId
GO

-- BACKUP PROCEDURE
CREATE PROCEDURE back_up
AS
BACKUP DATABASE hastane
TO DISK = 'D:\';
 GO
							
											-- TRIGGERS
-- INSERT TRIGGERS
CREATE TRIGGER hastaKaydiReply
	on hasta
	AFTER INSERT
AS
BEGIN
	SELECT 'YENI HASTA EKLENDI' AS REPLY
END	

drop trigger hastaKaydiReply


CREATE TRIGGER users_kayit_reply
	on users
	AFTER INSERT
AS
BEGIN
	SELECT 'YENI KULLANICI EKLENDI' AS REPLY
END

CREATE TRIGGER doktor_kayit_reply
	on doktor
	AFTER INSERT
AS
BEGIN
	SELECT 'YENI DOKTOR EKLENDI' AS REPLY
END	

CREATE TRIGGER muayene_kayit_reply
	on muayene
	AFTER INSERT
AS
BEGIN
	SELECT 'YENI MUAYENE BILGISI EKLENDI' AS REPLY
END	

CREATE TRIGGER muayeneSonuc_reply
	on muayeneSonuc
	AFTER INSERT
AS
BEGIN
	SELECT 'MUAYENE BILGILERI EKLENDI' AS REPLY
END	

CREATE TRIGGER ameliyat_reply
	on ameliyat
	AFTER INSERT
AS
BEGIN
	SELECT 'AMELIYAT BILGILERI EKLENDI' AS REPLY
END	


-- UPDATE


CREATE TRIGGER hastaUpdateReply
	on hasta
	AFTER UPDATE
AS
BEGIN
	SELECT ' HASTA KAYIT GUNCELLEME BASARILI'
END

CREATE TRIGGER doktorUpdateReply
	on doktor
	AFTER UPDATE
AS
BEGIN
	SELECT ' DOKTOR KAYIT GUNCELLEME BASARILI'
END

CREATE TRIGGER kullaniciGuncellemeReply
	on users
	AFTER UPDATE
AS
BEGIN
	SELECT 'KULLANICI KAYIT GUNCELLEME BASARILI'
END

CREATE TRIGGER muayeneGuncellemeReply
	on muayene
	AFTER UPDATE
AS
BEGIN
	SELECT 'MUAYENE BILGI GUNCELLEME BASARILI'
END

CREATE TRIGGER muayeneSonucReply
	on muayeneSonuc
	AFTER UPDATE
AS
BEGIN
	SELECT ' MUAYENE SONUC GUNCELLEME BASARILI'
END

CREATE TRIGGER ameliyatUpdateReply
	on ameliyat
	AFTER UPDATE
AS
BEGIN
	SELECT ' AMELIYAT KAYIT GUNCELLEME BASARILI'
END


-- DELETE
CREATE TRIGGER silinenkayitlog
	on hasta
	AFTER DELETE
AS
BEGIN
DECLARE @Id bigint
DECLARE @ad varchar(20)
DECLARE @soyad varchar(20)
DECLARE @adres varchar(255)
DECLARE @CepTel varchar(10)
DECLARE @tcno varchar(11)
DECLARE @cinsiyet char(5)
DECLARE @kayittar date
DECLARE @kanGrubu varchar(20)
DECLARE @dogTar date
DECLARE @dogYer varchar(20)
SELECT @Id=hastaId from DELETED
SELECT @ad=hasta_ad from DELETED
SELECT @soyad=hasta_soyad from DELETED
SELECT @adres=hasta_adres from DELETED
SELECT @CepTel=hasta_CepTel from DELETED
SELECT @tcno=hasta_tcno from DELETED
SELECT @cinsiyet=hasta_cinsiyet from DELETED
SELECT @kayittar=hasta_kayittar from DELETED
SELECT @kanGrubu=hasta_kanGrubu from DELETED
SELECT @dogTar=hasta_dogTar from DELETED
SELECT @dogYer=hasta_dogYer from DELETED
	INSERT silinmis_hasta_kayitlari (hastaId,hasta_ad,hasta_soyad,hasta_adres,hasta_CepTel,hasta_tcno,hasta_cinsiyet,hasta_kayittar,hasta_kanGrubu,hasta_dogTar,hasta_dogYer) VALUES (@Id,@ad,@soyad,@adres,@CepTel,@tcno,@cinsiyet,@kayittar,@kanGrubu,@dogTar,@dogYer)
END
CREATE TRIGGER doktor_silinen_kayit
	on doktor
	AFTER DELETE
AS
BEGIN
DECLARE @id smallint
DECLARE @ad varchar(20)
DECLARE @soyad varchar(20)
DECLARE @unvan varchar(20)
DECLARE @cinsiyet char(5)
DECLARE @dogtar date
SELECT @id=doktorId from DELETED
SELECT @ad=doc_ad from DELETED
SELECT @soyad=doc_soyad from DELETED
SELECT @unvan=doc_unvan from DELETED
SELECT @cinsiyet=doc_cinsiyet from DELETED
SELECT @dogtar=doc_DogTar from DELETED
	INSERT silinmis_doktor_kayitlari (doktorId,doktor_ad,doktor_soyad,doktor_unvan,doktor_cinsiyet,doktor_dogTar) VALUES (@id,@ad,@soyad,@unvan,@cinsiyet,@dogtar)
END

CREATE TRIGGER muayene_silinen_kayit
	on muayene
	AFTER DELETE
AS
BEGIN
DECLARE @mid int
DECLARE @hid smallint
DECLARE @mdate date
DECLARE @mtime time
DECLARE @did smallint
DECLARE @mtype varchar(30)
SELECT @mid=muayeneId from DELETED
SELECT @hid=hastaId from DELETED
SELECT @mdate=muayeneTar from DELETED
SELECT @mtime=muayeneSaat from DELETED
SELECT @did=doktorId from DELETED
SELECT @mtype=muayeneTuru from DELETED
	INSERT silinmis_muayene_kayitlari (muayeneId,hastaId,muayeneTar,MuayeneSaat,doktorId,muayeneTuru) VALUES (@mid,@hid,@mdate,@mtime,@did,@mtype)
END
CREATE TRIGGER hastaDeleteReply
	on hasta
	AFTER DELETE
AS
BEGIN
	SELECT 'HASTA KAYDI SILINDI'
END

CREATE TRIGGER doktor_delete_reply
	on doktor
	AFTER DELETE
AS
BEGIN
	SELECT 'DOKTOR KAYDI SILINDI'
END

CREATE TRIGGER user_delete_reply
	on users
	AFTER DELETE
AS
BEGIN
	SELECT 'KULLANICI KAYDI SILINDI'
END

CREATE TRIGGER muayene_delete_reply
	on muayene
	AFTER DELETE
AS
BEGIN
	SELECT 'MUAYENE KAYDI SILINDI'
END

CREATE TRIGGER muayene_Sonuc_delete_reply
	on muayeneSonuc
	AFTER DELETE
AS
BEGIN
	SELECT 'MUAYENE SONUC KAYDI SILINDI'
END

CREATE TRIGGER ameliyat_delete_reply
	on ameliyat
	AFTER DELETE
AS
BEGIN
	SELECT 'AMELIYAT KAYDI SILINDI'
END


-- INSTEAD OF

CREATE TRIGGER InsteadOfDeleteTrigger
ON users
INSTEAD OF DELETE
AS 
	SELECT ('KULLANICI TABLOSU UZERINDE SILME ISLEMI YAPAMAZSINIZ!')  	
GO
-- FOR

CREATE TRIGGER doktoreklecevap
	on doktor
	FOR INSERT
AS
BEGIN
	SELECT 'YENI DOKTOR EKLENDI' AS REPLY
END	


	
	INSERT users VALUES ('admin','admin','Admin')
	INSERT users VALUES ('selim','selim')
	INSERT doktor VALUES ('namik','kemal','profesor','erkek','05.19.1965')
	INSERT hasta (hasta_ad,hasta_soyad,hasta_adres,hasta_CepTel,hasta_tcno,hasta_cinsiyet,hasta_kanGrubu,hasta_dogTar,hasta_dogYer) VALUES ('selim','aslan','DUZCE / MERKEZ','5555555555','12345678943','ERKEK','AB+','05.19.1998','Mersin')
	INSERT muayene (hastaId,doktorId) VALUES (100,500)
	INSERT muayeneSonuc VALUES (300,100,'hasta oldu olucek')
	INSERT ameliyat VALUES ('bicme ameliyati','kesicez bicicez','2222',100,500)




select * from users
select * from hasta
select * from muayene
select * from muayeneSonuc
select * from doktor
select * from ameliyat
select * from silinmis_hasta_kayitlari

truncate table users
truncate table hasta
truncate table muayene
truncate table muayeneSonuc
truncate table doktor
truncate table ameliyat


select m.hastaId,ad,soyad,adres,CepTel,tcno,m.muayeneId,m.muayeneTar,m.DoktorId from hasta inner join muayene m on hasta.hastaId = m.hastaId --join doktor d on d.doktorId = m.doktorId
select m.hastaId,ad,soyad,tcno,cinsiyet,kanGrubu,m.muayeneTar,ms.aciklama,a.ameliyataciklama,a.ameliyatturu,a.ameliyatucret from hasta inner join muayene m on hasta.hastaId = m.hastaId join muayeneSonuc ms on m.muayeneId = ms.muayeneId join ameliyat a on a.hastaId = hasta.hastaId



select hasta_ad AS 'ADI',hasta_soyad AS 'SOYADI',hasta_tcno AS 'TCNO',hasta_cinsiyet AS 'CINSIYET',hasta_kanGrubu AS 'KAN GRUBU',hasta_dogTar AS 'DOGUM TARIHI',m.muayeneTar as 'MUAYENE TARIHI',m.muayeneSaat AS 'MUAYENE SAATI',ms.aciklama AS 'SONUC' from hasta h join muayene m on h.hastaId=m.hastaId join muayeneSonuc ms on h.hastaId=ms.hastaId

-- HASTA MUAYENE BILGISI GETIRME
select hasta_ad AS 'ADI',hasta_soyad AS 'SOYADI',hasta_tcno AS 'TCNO',hasta_cinsiyet AS 'CINSIYET',hasta_kanGrubu AS 'KAN GRUBU',hasta_dogTar AS 'DOGUM TARIHI',
	d.doc_ad AS 'DOKTORUN ADI',d.doc_soyad AS 'DOKTORUN SOYADI',m.muayeneTar as 'MUAYENE TARIHI',m.muayeneSaat AS 'MUAYENE SAATI',ms.aciklama AS 'SONUC' 
		from hasta h join muayene m on h.hastaId=m.hastaId join doktor d on d.doktorId=m.doktorId join muayeneSonuc ms on m.muayeneId=ms.muayeneId


CREATE PROCEDURE back_up
AS
BEGIN
BACKUP DATABASE [hastane] 
TO  DISK = N'C:\Program Files\Microsoft SQL Server\MSSQL14.SQLSCA\MSSQL\Backup\hastane.bak' 
WITH NOFORMAT, NOINIT,  NAME = N'hastane-Full Database Backup', SKIP, NOREWIND, NOUNLOAD,  STATS = 10
END
GO

EXEC back_up

drop procedure while_loop

CREATE PROCEDURE while_loop
AS
BEGIN
DECLARE @count bigint;
DECLARE @telno bigint;
DECLARE @tcno bigint;
SET @tcno = 21111111111;
SET @telno = 1111111111;
SET @count = 1;
    
WHILE @count<= 250000
BEGIN
	INSERT INTO hasta (hasta_ad,hasta_soyad,hasta_adres,hasta_CepTel,hasta_tcno,hasta_cinsiyet,hasta_kanGrubu,hasta_dogTar,hasta_dogYer) VALUES ('selim','aslan','DUZCE / MERKEZ',@telno+1,@tcno+1,'ERKEK','AB+','05.19.1998','Mersin')
    SET @count = @count + 1;
	SET @tcno = @tcno + 1;
	SET @telno = @telno + 1;
END;
END

EXEC while_loop

delete from hasta
select *from hasta
CREATE PROCEDURE row_sayisi
AS
BEGIN
SELECT 
    COUNT(*) hastaId
FROM
    hasta;
END

exec row_sayisi

CREATE PROCEDURE restore_back_up
AS
BACKUP LOG [hastane] TO  DISK = N'C:\Program Files\Microsoft SQL Server\MSSQL14.SQLSCA\MSSQL\Backup\hastane_LogBackup_2019-12-23_13-44-31.bak' WITH NOFORMAT, NOINIT,  NAME = N'hastane_LogBackup_2019-12-23_13-44-31', NOSKIP, NOREWIND, NOUNLOAD,  NORECOVERY ,  STATS = 5
RESTORE DATABASE [hastane] FROM  DISK = N'C:\Program Files\Microsoft SQL Server\MSSQL14.SQLSCA\MSSQL\Backup\hastane.bak' WITH  FILE = 1,  NOUNLOAD,  STATS = 5
GO



EXEC restore_back_up

USE [master]
RESTORE DATABASE [student] FROM  DISK = N'C:\Program Files\Microsoft SQL Server\MSSQL14.SQLSCA\MSSQL\Backup\student.bak' WITH  FILE = 1,  NOUNLOAD,  STATS = 5

GO

drop database hastane

select * from users