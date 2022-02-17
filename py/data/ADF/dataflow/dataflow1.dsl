source(output(
		ID as short,
		product_tag as string,
		market_long_description as string,
		market_short_description as string,
		country as string,
		sales_units as integer,
		sales_units_yrago as integer,
		sales_volume as integer
	),
	allowSchemaDrift: true,
	validateSchema: false,
	ignoreNoFilesFound: false,
	format: 'excel',
	container: 'synapseconverter',
	fileName: 'IRI_join1.xlsx',
	sheetName: 'Sheet1',
	firstRowAsHeader: true) ~> source1
source(output(
		ID as short,
		product_tag as string,
		market_long_description as string,
		market_short_description as string,
		country as string,
		sales_units as integer,
		sales_units_yrago as integer,
		sales_volume as integer
	),
	allowSchemaDrift: true,
	validateSchema: false,
	ignoreNoFilesFound: false,
	format: 'excel',
	container: 'synapseconverter',
	fileName: 'IRI_join2.xlsx',
	sheetName: 'Sheet1',
	firstRowAsHeader: true) ~> source2
source1, source2 join(source1@ID == source2@ID,
	joinType:'inner',
	broadcast: 'auto')~> Join1
Join1 sink(allowSchemaDrift: true,
	validateSchema: false,
	format: 'table',
	store: 'sqlserver',
	schemaName: 'dbo',
	tableName: 'Cameleon_Table_Cross',
	insertable: true,
	updateable: false,
	deletable: false,
	upsertable: false,
	skipDuplicateMapInputs: true,
	skipDuplicateMapOutputs: true,
	errorHandlingOption: 'stopOnFirstError') ~> sink1