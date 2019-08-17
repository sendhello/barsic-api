# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Accountstock(models.Model):
    accountstockid = models.AutoField(db_column='AccountStockId', primary_key=True)  # Field name made lowercase.
    superaccountid = models.ForeignKey('Superaccount', models.DO_NOTHING,
                                       db_column='SuperAccountId')  # Field name made lowercase.
    stocktype = models.SmallIntegerField(db_column='StockType')  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    categoryid = models.ForeignKey('Category', models.DO_NOTHING, db_column='CategoryId', blank=True,
                                   null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=18, decimal_places=2, blank=True,
                                 null=True)  # Field name made lowercase.
    start = models.DateTimeField(db_column='Start', blank=True, null=True)  # Field name made lowercase.
    end = models.DateTimeField(db_column='End', blank=True, null=True)  # Field name made lowercase.
    istimepatternapplied = models.BooleanField(db_column='IsTimePatternApplied', blank=True,
                                               null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=50, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    targetaccountstockid = models.IntegerField(db_column='TargetAccountStockId', blank=True,
                                               null=True)  # Field name made lowercase.
    ticketnumber = models.IntegerField(db_column='TicketNumber', blank=True, null=True)  # Field name made lowercase.
    ticketset = models.CharField(db_column='TicketSet', max_length=5, blank=True,
                                 null=True)  # Field name made lowercase.
    passesdone = models.IntegerField(db_column='PassesDone', blank=True, null=True)  # Field name made lowercase.
    tilldate = models.DateTimeField(db_column='TillDate', blank=True, null=True)  # Field name made lowercase.
    number = models.IntegerField(db_column='Number', blank=True, null=True)  # Field name made lowercase.
    prebookedtill = models.DateTimeField(db_column='PreBookedTill', blank=True, null=True)  # Field name made lowercase.
    prebookeduserid = models.ForeignKey('Secsubject', models.DO_NOTHING, db_column='PreBookedUserId', blank=True,
                                        null=True)  # Field name made lowercase.
    keyownerid = models.IntegerField(db_column='KeyOwnerId', blank=True, null=True)  # Field name made lowercase.
    activitybookinginfoid = models.ForeignKey('Activitybookinginfo', models.DO_NOTHING,
                                              db_column='ActivityBookingInfoId', blank=True,
                                              null=True)  # Field name made lowercase.
    expectedexittime = models.DateTimeField(db_column='ExpectedExitTime', blank=True,
                                            null=True)  # Field name made lowercase.
    lastuse = models.DateTimeField(db_column='LastUse', blank=True, null=True)  # Field name made lowercase.
    externalid = models.IntegerField(db_column='ExternalId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccountStock'


class Accounttag(models.Model):
    accounttagid = models.AutoField(db_column='AccountTagId', primary_key=True)  # Field name made lowercase.
    ownerid = models.IntegerField(db_column='OwnerId')  # Field name made lowercase.
    tagid = models.ForeignKey('Tag', models.DO_NOTHING, db_column='TagId')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=18, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccountTag'


class Activity(models.Model):
    activityid = models.AutoField(db_column='ActivityId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    parentid = models.IntegerField(db_column='ParentId', blank=True, null=True)  # Field name made lowercase.
    categoryid = models.ForeignKey('Category', models.DO_NOTHING, db_column='CategoryId', blank=True,
                                   null=True)  # Field name made lowercase.
    calendarid = models.ForeignKey('Calendar', models.DO_NOTHING, db_column='CalendarId', blank=True,
                                   null=True)  # Field name made lowercase.
    reserveminutes = models.IntegerField(db_column='ReserveMinutes', blank=True,
                                         null=True)  # Field name made lowercase.
    depth = models.IntegerField(db_column='Depth', blank=True, null=True)  # Field name made lowercase.
    extendeddata = models.TextField(db_column='ExtendedData', blank=True, null=True)  # Field name made lowercase.
    onlinetempleateid = models.ForeignKey('Shablonscardprinter', models.DO_NOTHING, db_column='OnlineTempleateId',
                                          blank=True, null=True)  # Field name made lowercase.
    sellwithoutscheme = models.BooleanField(db_column='SellWithoutScheme')  # Field name made lowercase.
    placereservetimelimit = models.IntegerField(db_column='PlaceReserveTimeLimit', blank=True,
                                                null=True)  # Field name made lowercase.
    reservetemplateid = models.IntegerField(db_column='ReserveTemplateId', blank=True,
                                            null=True)  # Field name made lowercase.
    allowselldaysbefore = models.IntegerField(db_column='AllowSellDaysBefore', blank=True,
                                              null=True)  # Field name made lowercase.
    allowsellfrom = models.DateTimeField(db_column='AllowSellFrom', blank=True, null=True)  # Field name made lowercase.
    allowsellto = models.DateTimeField(db_column='AllowSellTo', blank=True, null=True)  # Field name made lowercase.
    independentschedules = models.BooleanField(db_column='IndependentSchedules')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Activity'


class Activitybookinginfo(models.Model):
    activitybookinginfoid = models.AutoField(db_column='ActivityBookingInfoId',
                                             primary_key=True)  # Field name made lowercase.
    activityscheduleid = models.ForeignKey('Activityschedule', models.DO_NOTHING, db_column='ActivityScheduleId',
                                           blank=True, null=True)  # Field name made lowercase.
    placeid = models.ForeignKey('Place', models.DO_NOTHING, db_column='PlaceId', blank=True,
                                null=True)  # Field name made lowercase.
    prebookedtill = models.DateTimeField(db_column='PreBookedTill', blank=True, null=True)  # Field name made lowercase.
    bookingstatus = models.IntegerField(db_column='BookingStatus', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    placereserveid = models.ForeignKey('Placereserve', models.DO_NOTHING, db_column='PlaceReserveId', blank=True,
                                       null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ActivityBookingInfo'


class Activityschedule(models.Model):
    activityscheduleid = models.AutoField(db_column='ActivityScheduleId',
                                          primary_key=True)  # Field name made lowercase.
    activityid = models.ForeignKey(Activity, models.DO_NOTHING, db_column='ActivityId', blank=True,
                                   null=True)  # Field name made lowercase.
    placeid = models.ForeignKey('Place', models.DO_NOTHING, db_column='PlaceId', blank=True,
                                null=True)  # Field name made lowercase.
    datefrom = models.DateTimeField(db_column='DateFrom', blank=True, null=True)  # Field name made lowercase.
    dateto = models.DateTimeField(db_column='DateTo', blank=True, null=True)  # Field name made lowercase.
    nextactivityscheduleid = models.IntegerField(db_column='NextActivityScheduleId', blank=True,
                                                 null=True)  # Field name made lowercase.
    isallowsplit = models.BooleanField(db_column='IsAllowSplit', blank=True, null=True)  # Field name made lowercase.
    reservequantity = models.IntegerField(db_column='ReserveQuantity', blank=True,
                                          null=True)  # Field name made lowercase.
    islastforbooking = models.BooleanField(db_column='IsLastForBooking', blank=True,
                                           null=True)  # Field name made lowercase.
    luftminutesafterend = models.IntegerField(db_column='LuftMinutesAfterEnd', blank=True,
                                              null=True)  # Field name made lowercase.
    seasontemplateid = models.IntegerField(db_column='SeasonTemplateId', blank=True,
                                           null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ActivitySchedule'


class Agreement(models.Model):
    agreementid = models.AutoField(db_column='AgreementId', primary_key=True)  # Field name made lowercase.
    agreementtypeid = models.ForeignKey('Agreementtype', models.DO_NOTHING,
                                        db_column='AgreementTypeId')  # Field name made lowercase.
    from_field = models.DateTimeField(db_column='From', blank=True,
                                      null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    to = models.DateTimeField(db_column='To', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('Secsubject', models.DO_NOTHING, db_column='UserId', blank=True,
                               null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.
    superaccountid = models.ForeignKey('Superaccount', models.DO_NOTHING,
                                       db_column='SuperAccountId')  # Field name made lowercase.
    extendeddata = models.TextField(db_column='ExtendedData', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Agreement'


class Agreementtype(models.Model):
    agreementtypeid = models.AutoField(db_column='AgreementTypeId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    tagid = models.ForeignKey('Tag', models.DO_NOTHING, db_column='TagId', blank=True,
                              null=True)  # Field name made lowercase.
    extendeddata = models.TextField(db_column='ExtendedData', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AgreementType'


class Auditcfg(models.Model):
    savedeventtypes = models.IntegerField()
    savedeventimportances = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'AuditCfg'


class Booking(models.Model):
    bookingid = models.AutoField(db_column='BookingId', primary_key=True)  # Field name made lowercase.
    targetid = models.IntegerField(db_column='TargetId')  # Field name made lowercase.
    targettype = models.SmallIntegerField(db_column='TargetType')  # Field name made lowercase.
    scope = models.IntegerField(db_column='Scope')  # Field name made lowercase.
    cancross = models.BooleanField(db_column='CanCross')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Booking'


class Bookingspan(models.Model):
    bookingspanid = models.AutoField(db_column='BookingSpanId', primary_key=True)  # Field name made lowercase.
    bookingid = models.ForeignKey(Booking, models.DO_NOTHING, db_column='BookingId')  # Field name made lowercase.
    spanfrom = models.DateTimeField(db_column='SpanFrom')  # Field name made lowercase.
    spanto = models.DateTimeField(db_column='SpanTo', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=18, decimal_places=2, blank=True,
                                 null=True)  # Field name made lowercase.
    clientaccountstockid = models.IntegerField(db_column='ClientAccountStockId', blank=True,
                                               null=True)  # Field name made lowercase.
    spanpaidto = models.DateTimeField(db_column='SpanPaidTo', blank=True, null=True)  # Field name made lowercase.
    bookingmode = models.IntegerField(db_column='BookingMode', blank=True, null=True)  # Field name made lowercase.
    cardcode = models.CharField(db_column='CardCode', max_length=32, blank=True,
                                null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BookingSpan'


class Bookingspantag(models.Model):
    tagid = models.ForeignKey('Tag', models.DO_NOTHING, db_column='TagId')  # Field name made lowercase.
    bookingspanid = models.ForeignKey(Bookingspan, models.DO_NOTHING,
                                      db_column='BookingSpanId')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=18, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BookingSpanTag'


class Calendar(models.Model):
    calendarid = models.IntegerField(db_column='CalendarId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    start = models.DateTimeField(db_column='Start')  # Field name made lowercase.
    end = models.DateTimeField(db_column='End')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Calendar'


class Calendarday(models.Model):
    calendardayid = models.IntegerField(db_column='CalendarDayId', primary_key=True)  # Field name made lowercase.
    daytypeid = models.ForeignKey('Daytype', models.DO_NOTHING, db_column='DayTypeId')  # Field name made lowercase.
    calendarid = models.ForeignKey(Calendar, models.DO_NOTHING, db_column='CalendarId')  # Field name made lowercase.
    datetime = models.DateTimeField(db_column='DateTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CalendarDay'


class Category(models.Model):
    categoryid = models.IntegerField(db_column='CategoryId', primary_key=True)  # Field name made lowercase.
    stocktype = models.SmallIntegerField(db_column='StockType')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    timepatternid = models.ForeignKey('Timepattern', models.DO_NOTHING, db_column='TimePatternId', blank=True,
                                      null=True)  # Field name made lowercase.
    timedelay = models.FloatField(db_column='TimeDelay', blank=True, null=True)  # Field name made lowercase.
    pattern = models.CharField(db_column='Pattern', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sellaction = models.IntegerField(db_column='SellAction', blank=True, null=True)  # Field name made lowercase.
    ispercent = models.BooleanField(db_column='IsPercent', blank=True, null=True)  # Field name made lowercase.
    prepayamount = models.DecimalField(db_column='PrepayAmount', max_digits=18, decimal_places=2, blank=True,
                                       null=True)  # Field name made lowercase.
    maxtimes = models.IntegerField(db_column='MaxTimes', blank=True, null=True)  # Field name made lowercase.
    codeemittype = models.IntegerField(db_column='CodeEmitType', blank=True, null=True)  # Field name made lowercase.
    codelength = models.IntegerField(db_column='CodeLength', blank=True, null=True)  # Field name made lowercase.
    codeprefix = models.CharField(db_column='CodePrefix', max_length=50, blank=True,
                                  null=True)  # Field name made lowercase.
    payonread = models.BooleanField(db_column='PayOnRead', blank=True, null=True)  # Field name made lowercase.
    tagid = models.ForeignKey('Tag', models.DO_NOTHING, db_column='TagId', blank=True,
                              null=True)  # Field name made lowercase.
    onetime = models.BooleanField(db_column='OneTime', blank=True, null=True)  # Field name made lowercase.
    moneypolitics = models.IntegerField(db_column='MoneyPolitics')  # Field name made lowercase.
    expectedexitminutes = models.FloatField(db_column='ExpectedExitMinutes')  # Field name made lowercase.
    days = models.IntegerField(db_column='Days', blank=True, null=True)  # Field name made lowercase.
    passes = models.IntegerField(db_column='Passes', blank=True, null=True)  # Field name made lowercase.
    accesscode = models.IntegerField(db_column='AccessCode', blank=True, null=True)  # Field name made lowercase.
    displayformat = models.CharField(db_column='DisplayFormat', max_length=50, blank=True,
                                     null=True)  # Field name made lowercase.
    allowautosell = models.BooleanField(db_column='AllowAutoSell', blank=True, null=True)  # Field name made lowercase.
    ruleid = models.ForeignKey('Rule', models.DO_NOTHING, db_column='RuleId', blank=True,
                               null=True)  # Field name made lowercase.
    linkedcategoryid = models.ForeignKey('self', models.DO_NOTHING, db_column='LinkedCategoryId', blank=True,
                                         null=True)  # Field name made lowercase.
    nn = models.CharField(db_column='NN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    allwaysgenerate = models.BooleanField(db_column='AllwaysGenerate', blank=True,
                                          null=True)  # Field name made lowercase.
    cardgenerratealgorithm = models.IntegerField(db_column='CardGenerrateAlgorithm', blank=True,
                                                 null=True)  # Field name made lowercase.
    reportweight = models.FloatField(db_column='ReportWeight', blank=True, null=True)  # Field name made lowercase.
    tag2id = models.ForeignKey('Tag', models.DO_NOTHING, db_column='Tag2Id', related_name='tag2id', blank=True,
                               null=True)  # Field name made lowercase.
    extendeddata = models.TextField(db_column='ExtendedData', blank=True, null=True)  # Field name made lowercase.
    seasontemplateid = models.ForeignKey('Seasontemplate', models.DO_NOTHING, db_column='SeasonTemplateId', blank=True,
                                         null=True)  # Field name made lowercase.
    vat = models.IntegerField(db_column='Vat')  # Field name made lowercase.
    vatpercent = models.DecimalField(db_column='VatPercent', max_digits=18, decimal_places=2, blank=True,
                                     null=True)  # Field name made lowercase.
    personalinforequirment = models.IntegerField(db_column='PersonalInfoRequirment')  # Field name made lowercase.
    section = models.IntegerField(db_column='Section')  # Field name made lowercase.
    priority = models.IntegerField(db_column='Priority', blank=True, null=True)  # Field name made lowercase.
    taxsystem = models.IntegerField(db_column='TaxSystem')  # Field name made lowercase.
    subjecttype = models.IntegerField(db_column='SubjectType', blank=True, null=True)  # Field name made lowercase.
    organizationid = models.ForeignKey('Superaccount', models.DO_NOTHING, db_column='OrganizationId', blank=True,
                                       null=True)  # Field name made lowercase.
    ispromotional = models.BooleanField(db_column='IsPromotional')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Category'


class Check(models.Model):
    checkid = models.AutoField(db_column='CheckId', primary_key=True)  # Field name made lowercase.
    typeoper = models.SmallIntegerField(db_column='TypeOper', blank=True, null=True)  # Field name made lowercase.
    cassa = models.SmallIntegerField(db_column='Cassa', blank=True, null=True)  # Field name made lowercase.
    smena = models.SmallIntegerField(db_column='Smena', blank=True, null=True)  # Field name made lowercase.
    nomer = models.SmallIntegerField(db_column='Nomer', blank=True, null=True)  # Field name made lowercase.
    summa = models.DecimalField(db_column='Summa', max_digits=19, decimal_places=4, blank=True,
                                null=True)  # Field name made lowercase.
    nal = models.DecimalField(db_column='Nal', max_digits=19, decimal_places=4, blank=True,
                              null=True)  # Field name made lowercase.
    beznal = models.DecimalField(db_column='Beznal', max_digits=19, decimal_places=4, blank=True,
                                 null=True)  # Field name made lowercase.
    chet = models.DecimalField(db_column='Chet', max_digits=19, decimal_places=4, blank=True,
                               null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    error = models.IntegerField(db_column='Error', blank=True, null=True)  # Field name made lowercase.
    texterror = models.CharField(db_column='TextError', max_length=100, blank=True,
                                 null=True)  # Field name made lowercase.
    data = models.DateTimeField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    bonus = models.DecimalField(db_column='Bonus', max_digits=19, decimal_places=4, blank=True,
                                null=True)  # Field name made lowercase.
    bonustoadd = models.DecimalField(db_column='BonusToAdd', max_digits=19, decimal_places=4, blank=True,
                                     null=True)  # Field name made lowercase.
    card = models.CharField(db_column='Card', max_length=50, blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId', blank=True, null=True)  # Field name made lowercase.
    kkmid = models.ForeignKey('Kkm', models.DO_NOTHING, db_column='KkmId', blank=True,
                              null=True)  # Field name made lowercase.
    zcounter = models.DecimalField(db_column='ZCounter', max_digits=18, decimal_places=2, blank=True,
                                   null=True)  # Field name made lowercase.
    zreturns = models.DecimalField(db_column='ZReturns', max_digits=18, decimal_places=2, blank=True,
                                   null=True)  # Field name made lowercase.
    zsells = models.DecimalField(db_column='ZSells', max_digits=18, decimal_places=2, blank=True,
                                 null=True)  # Field name made lowercase.
    zsmena = models.IntegerField(db_column='ZSmena', blank=True, null=True)  # Field name made lowercase.
    currency = models.DecimalField(db_column='Currency', max_digits=19, decimal_places=4, blank=True,
                                   null=True)  # Field name made lowercase.
    extendeddata = models.TextField(db_column='ExtendedData', blank=True, null=True)  # Field name made lowercase.
    datekkt = models.DateTimeField(db_column='DateKKT', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=50, blank=True, null=True)
    fpd = models.CharField(db_column='FPD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(max_length=20, blank=True, null=True)
    regnumkkt = models.CharField(db_column='RegNumKKT', max_length=16, blank=True,
                                 null=True)  # Field name made lowercase.
    numberfn = models.CharField(db_column='NumberFN', max_length=16, blank=True,
                                null=True)  # Field name made lowercase.
    sendstateemail = models.SmallIntegerField(db_column='SendStateEmail')  # Field name made lowercase.
    sendstatesms = models.SmallIntegerField(db_column='SendStateSms')  # Field name made lowercase.
    emailsendattempts = models.SmallIntegerField(db_column='EmailSendAttempts')  # Field name made lowercase.
    smssendattempts = models.SmallIntegerField(db_column='SmsSendAttempts')  # Field name made lowercase.
    inn = models.CharField(db_column='INN', max_length=12, blank=True, null=True)  # Field name made lowercase.
    numberfd = models.IntegerField(db_column='NumberFD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Check'


class Checkdetail(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    checkid = models.ForeignKey(Check, models.DO_NOTHING, db_column='CheckId')  # Field name made lowercase.
    mastertransactionid = models.IntegerField(db_column='MasterTransactionId', blank=True,
                                              null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200, blank=True, null=True)  # Field name made lowercase.
    count = models.DecimalField(db_column='Count', max_digits=18, decimal_places=3, blank=True,
                                null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=18, decimal_places=2, blank=True,
                                null=True)  # Field name made lowercase.
    cardcode = models.CharField(db_column='CardCode', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    categoryid = models.ForeignKey(Category, models.DO_NOTHING, db_column='CategoryId', blank=True,
                                   null=True)  # Field name made lowercase.
    isdebtclose = models.BooleanField(db_column='IsDebtClose')  # Field name made lowercase.
    extendeddata = models.TextField(db_column='ExtendedData', blank=True, null=True)  # Field name made lowercase.
    typegood = models.IntegerField(db_column='TypeGood', blank=True, null=True)  # Field name made lowercase.
    returncheckdetailid = models.ForeignKey('self', models.DO_NOTHING, db_column='ReturnCheckDetailId', blank=True,
                                            null=True)  # Field name made lowercase.
    vat = models.IntegerField(db_column='Vat')  # Field name made lowercase.
    vatpercent = models.IntegerField(db_column='VatPercent', blank=True, null=True)  # Field name made lowercase.
    section = models.IntegerField(db_column='Section')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CheckDetail'


class Checkpay(models.Model):
    checkid = models.ForeignKey(Check, models.DO_NOTHING, db_column='CheckId')  # Field name made lowercase.
    checkpaytypeid = models.ForeignKey('Checkpaytype', models.DO_NOTHING,
                                       db_column='CheckPayTypeId')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=18, decimal_places=2)  # Field name made lowercase.
    extendeddata = models.TextField(db_column='ExtendedData', blank=True, null=True)  # Field name made lowercase.
    referenceno = models.CharField(db_column='ReferenceNo', max_length=50, blank=True,
                                   null=True)  # Field name made lowercase.
    payerclientid = models.ForeignKey('Superaccount', models.DO_NOTHING, db_column='PayerClientId', blank=True,
                                      null=True)  # Field name made lowercase.
    externalpayerid = models.IntegerField(db_column='ExternalPayerId', blank=True,
                                          null=True)  # Field name made lowercase.
    externalpayerreference = models.CharField(db_column='ExternalPayerReference', max_length=50, blank=True,
                                              null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CheckPay'


class Checkpaytype(models.Model):
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    isfiscal = models.BooleanField(db_column='IsFiscal')  # Field name made lowercase.
    printercode = models.IntegerField(db_column='PrinterCode')  # Field name made lowercase.
    processingtype = models.IntegerField(db_column='ProcessingType')  # Field name made lowercase.
    processingname = models.CharField(db_column='ProcessingName', max_length=50, blank=True,
                                      null=True)  # Field name made lowercase.
    issystem = models.BooleanField(db_column='IsSystem')  # Field name made lowercase.
    checkpaytypeid = models.AutoField(db_column='CheckPayTypeId', primary_key=True)  # Field name made lowercase.
    extendeddata = models.TextField(db_column='ExtendedData', blank=True, null=True)  # Field name made lowercase.
    noreturn = models.BooleanField(db_column='NoReturn')  # Field name made lowercase.
    isenabled = models.BooleanField(db_column='IsEnabled')  # Field name made lowercase.
    position = models.SmallIntegerField(db_column='Position')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CheckPayType'


class Checkprinttask(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created')  # Field name made lowercase.
    finished = models.DateTimeField(db_column='Finished', blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status')  # Field name made lowercase.
    externalid = models.CharField(db_column='ExternalId', max_length=50, blank=True,
                                  null=True)  # Field name made lowercase.
    profileid = models.SmallIntegerField(db_column='ProfileId')  # Field name made lowercase.
    data = models.CharField(db_column='Data', max_length=4000)  # Field name made lowercase.
    errorscount = models.SmallIntegerField(db_column='ErrorsCount')  # Field name made lowercase.
    lasterror = models.CharField(db_column='LastError', max_length=4000, blank=True,
                                 null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CheckPrintTask'


class Clientcategory(models.Model):
    clientcategoryid = models.AutoField(db_column='ClientCategoryId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    isadministrative = models.BooleanField(db_column='IsAdministrative')  # Field name made lowercase.
    accesscode = models.IntegerField(db_column='AccessCode', blank=True, null=True)  # Field name made lowercase.
    externalid = models.CharField(db_column='ExternalId', max_length=50, blank=True,
                                  null=True)  # Field name made lowercase.
    extebdeddata = models.TextField(db_column='ExtebdedData', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClientCategory'


class Codegeneration(models.Model):
    codegenerationid = models.BigAutoField(db_column='CodeGenerationId', primary_key=True)  # Field name made lowercase.
    user = models.CharField(db_column='User', max_length=50)  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CodeGeneration'


class Communicationport(models.Model):
    communicationportid = models.IntegerField(db_column='CommunicationPortId',
                                              primary_key=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.
    computerid = models.ForeignKey('Computer', models.DO_NOTHING, db_column='ComputerId')  # Field name made lowercase.
    number = models.IntegerField(db_column='Number', blank=True, null=True)  # Field name made lowercase.
    speed = models.IntegerField(db_column='Speed', blank=True, null=True)  # Field name made lowercase.
    ip = models.CharField(db_column='Ip', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ipport = models.IntegerField(db_column='IpPort', blank=True, null=True)  # Field name made lowercase.
    extendeddata = models.TextField(db_column='ExtendedData', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CommunicationPort'


class Computer(models.Model):
    computerid = models.IntegerField(db_column='ComputerId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    monitoringport = models.IntegerField(db_column='MonitoringPort')  # Field name made lowercase.
    extendeddata = models.TextField(db_column='ExtendedData', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Computer'


class Controller(models.Model):
    controllerid = models.IntegerField(db_column='ControllerId', primary_key=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.
    code = models.IntegerField(db_column='Code')  # Field name made lowercase.
    communicationportid = models.ForeignKey(Communicationport, models.DO_NOTHING,
                                            db_column='CommunicationPortId')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    indicationmask = models.IntegerField(db_column='IndicationMask')  # Field name made lowercase.
    extendeddata = models.TextField(db_column='ExtendedData', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Controller'


class CustomComment(models.Model):
    transid = models.IntegerField(db_column='TransID', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.
    superaccount = models.IntegerField(db_column='SuperAccount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Custom_Comment'


class Daytimeinterval(models.Model):
    daytimeintervalid = models.IntegerField(db_column='DayTimeIntervalId',
                                            primary_key=True)  # Field name made lowercase.
    start = models.DateTimeField(db_column='Start')  # Field name made lowercase.
    end = models.DateTimeField(db_column='End')  # Field name made lowercase.
    allow = models.BooleanField(db_column='Allow')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DayTimeInterval'


class Daytype(models.Model):
    daytypeid = models.IntegerField(db_column='DayTypeId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    color = models.IntegerField(db_column='Color')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DayType'


class Defect(models.Model):
    defectid = models.AutoField(db_column='DefectId', primary_key=True)  # Field name made lowercase.
    defectreasonid = models.ForeignKey('Defectreason', models.DO_NOTHING,
                                       db_column='DefectReasonId')  # Field name made lowercase.
    userid = models.ForeignKey('Secsubject', models.DO_NOTHING, db_column='UserId')  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time')  # Field name made lowercase.
    ticketnumber = models.IntegerField(db_column='TicketNumber')  # Field name made lowercase.
    ticketset = models.CharField(db_column='TicketSet', max_length=5)  # Field name made lowercase.
    cardcode = models.CharField(db_column='CardCode', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    newcardcode = models.CharField(db_column='NewCardCode', max_length=50, blank=True,
                                   null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Defect'


class Defectreason(models.Model):
    defectreasonid = models.AutoField(db_column='DefectReasonId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    action = models.SmallIntegerField(db_column='Action')  # Field name made lowercase.
    reprint = models.BooleanField(db_column='Reprint')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DefectReason'


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    datetime = models.DateTimeField()
    type = models.IntegerField()
    importance = models.IntegerField()
    userid = models.IntegerField()
    info = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Event'


class Externalseller(models.Model):
    externalsellerid = models.AutoField(db_column='ExternalSellerId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=200, blank=True, null=True)  # Field name made lowercase.
    extendeddata = models.TextField(db_column='ExtendedData', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ExternalSeller'


class Externalsellerpool(models.Model):
    externalsellerpoolid = models.IntegerField(db_column='ExternalSellerPoolId',
                                               primary_key=True)  # Field name made lowercase.
    accepttime = models.DateTimeField(db_column='AcceptTime')  # Field name made lowercase.
    data = models.TextField(db_column='Data')  # Field name made lowercase.
    report = models.TextField(db_column='Report')  # Field name made lowercase.
    direction = models.IntegerField(db_column='Direction')  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=200, blank=True, null=True)  # Field name made lowercase.
    extendeddata = models.TextField(db_column='ExtendedData', blank=True, null=True)  # Field name made lowercase.
    externalsellerid = models.ForeignKey(Externalseller, models.DO_NOTHING,
                                         db_column='ExternalSellerId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ExternalSellerPool'


class Geography(models.Model):
    geographyid = models.AutoField(db_column='GeographyId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Geography'


class Global(models.Model):
    globalid = models.BigIntegerField(db_column='GlobalId', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Global'


class Globalconfig(models.Model):
    config = models.TextField(db_column='Config')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'GlobalConfig'


class Globalid(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    stocktype = models.IntegerField(db_column='StockType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GlobalId'


class Goodprice(models.Model):
    goodpriceid = models.IntegerField(db_column='GoodPriceId', primary_key=True)  # Field name made lowercase.
    goodid = models.IntegerField(db_column='GoodId')  # Field name made lowercase.
    goodtype = models.IntegerField(db_column='GoodType')  # Field name made lowercase.
    daytypeid = models.IntegerField(db_column='DayTypeId')  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=18, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GoodPrice'


class Hardwareevent(models.Model):
    time = models.DateTimeField(db_column='Time')  # Field name made lowercase.
    eventtype = models.IntegerField(db_column='EventType')  # Field name made lowercase.
    servername = models.CharField(db_column='ServerName', max_length=50)  # Field name made lowercase.
    controllerid = models.IntegerField(db_column='ControllerId', blank=True, null=True)  # Field name made lowercase.
    readerid = models.IntegerField(db_column='ReaderId', blank=True, null=True)  # Field name made lowercase.
    rawdata = models.CharField(db_column='RawData', max_length=1000, blank=True,
                               null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId', blank=True, null=True)  # Field name made lowercase.
    workstationname = models.CharField(db_column='WorkstationName', max_length=50, blank=True,
                                       null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=300, blank=True, null=True)  # Field name made lowercase.
    card = models.CharField(db_column='Card', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HardwareEvent'


class Hotkey(models.Model):
    hotkeyid = models.AutoField(db_column='HotKeyId', primary_key=True)  # Field name made lowercase.
    shortcut = models.IntegerField(db_column='Shortcut')  # Field name made lowercase.
    stockid = models.ForeignKey(Category, models.DO_NOTHING, db_column='StockId')  # Field name made lowercase.
    stocktypeid = models.SmallIntegerField(db_column='StockTypeId')  # Field name made lowercase.
    servicepointid = models.ForeignKey('Servicepoint', models.DO_NOTHING,
                                       db_column='ServicepointId')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=18, decimal_places=2)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=100)  # Field name made lowercase.
    color1 = models.IntegerField(db_column='Color1', blank=True, null=True)  # Field name made lowercase.
    color2 = models.IntegerField(db_column='Color2', blank=True, null=True)  # Field name made lowercase.
    gradient = models.IntegerField(db_column='Gradient')  # Field name made lowercase.
    order = models.IntegerField(db_column='Order')  # Field name made lowercase.
    hotkeyextendeddata = models.TextField(db_column='HotKeyExtendedData', blank=True,
                                          null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HotKey'


class Inventory(models.Model):
    code = models.CharField(db_column='Code', max_length=50)  # Field name made lowercase.
    lastuse = models.DateTimeField(db_column='LastUse', blank=True, null=True)  # Field name made lowercase.
    inventorizationnumber = models.BigIntegerField(db_column='InventorizationNumber', blank=True,
                                                   null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    manufacter = models.CharField(db_column='Manufacter', max_length=50, blank=True,
                                  null=True)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=50, blank=True, null=True)  # Field name made lowercase.
    size = models.CharField(db_column='Size', max_length=10, blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=18, decimal_places=2, blank=True,
                                null=True)  # Field name made lowercase.
    accountstockid = models.OneToOneField(Accountstock, models.DO_NOTHING, db_column='AccountStockId',
                                          primary_key=True)  # Field name made lowercase.
    categoryid = models.ForeignKey(Category, models.DO_NOTHING, db_column='CategoryId')  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    stocktype = models.SmallIntegerField(db_column='StockType')  # Field name made lowercase.
    superaccountid = models.ForeignKey('Superaccount', models.DO_NOTHING,
                                       db_column='SuperAccountId')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=18, decimal_places=2)  # Field name made lowercase.
    externalid = models.IntegerField(db_column='ExternalId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Inventory'
        unique_together = (('code', 'superaccountid'),)


class Inventoryreservation(models.Model):
    inventoryreservationid = models.AutoField(db_column='InventoryReservationId',
                                              primary_key=True)  # Field name made lowercase.
    reservationorderid = models.ForeignKey('Reservationorder', models.DO_NOTHING, db_column='ReservationOrderId',
                                           blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=100, blank=True,
                                null=True)  # Field name made lowercase.
    displayname = models.CharField(db_column='DisplayName', max_length=100, blank=True,
                                   null=True)  # Field name made lowercase.
    size = models.CharField(db_column='Size', max_length=100, blank=True, null=True)  # Field name made lowercase.
    isgroup = models.BooleanField(db_column='IsGroup', blank=True, null=True)  # Field name made lowercase.
    targetstockid = models.IntegerField(db_column='TargetStockId', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=18, decimal_places=2, blank=True,
                                 null=True)  # Field name made lowercase.
    hasbeenredeemed = models.BooleanField(db_column='HasBeenRedeemed', blank=True,
                                          null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InventoryReservation'


class Inventoryreservationlimit(models.Model):
    inventoryreservationlimitid = models.AutoField(db_column='InventoryReservationLimitId',
                                                   primary_key=True)  # Field name made lowercase.
    procatcategoryid = models.IntegerField(db_column='ProcatCategoryId', blank=True,
                                           null=True)  # Field name made lowercase.
    size = models.CharField(db_column='Size', max_length=10, blank=True, null=True)  # Field name made lowercase.
    displayname = models.CharField(db_column='DisplayName', max_length=100, blank=True,
                                   null=True)  # Field name made lowercase.
    remainingamount = models.DecimalField(db_column='RemainingAmount', max_digits=18, decimal_places=2, blank=True,
                                          null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InventoryReservationLimit'


class Kassasost(models.Model):
    num_kass = models.SmallIntegerField(blank=True, null=True)
    smena = models.SmallIntegerField(blank=True, null=True)
    ncheck = models.SmallIntegerField(blank=True, null=True)
    nalin = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    beznalin = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    nalout = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    beznalout = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    vnes = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    vines = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    computername = models.CharField(db_column='ComputerName', max_length=50, blank=True,
                                    null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KassaSost'


class Kkm(models.Model):
    kkmid = models.AutoField(db_column='KkmId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    vendornumber = models.CharField(db_column='VendorNumber', max_length=50, blank=True,
                                    null=True)  # Field name made lowercase.
    registrationnumber = models.CharField(db_column='RegistrationNumber', max_length=50, blank=True,
                                          null=True)  # Field name made lowercase.
    superaccountid = models.ForeignKey('Superaccount', models.DO_NOTHING,
                                       db_column='SuperAccountId')  # Field name made lowercase.
    config = models.TextField(db_column='Config', blank=True,
                              null=True)  # Field name made lowercase. This field type is a guess.
    active = models.BooleanField(db_column='Active')  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kassasostid = models.ForeignKey(Kassasost, models.DO_NOTHING, db_column='KassaSostId', blank=True,
                                    null=True)  # Field name made lowercase.
    posnumber = models.IntegerField(db_column='PosNumber')  # Field name made lowercase.
    smena = models.IntegerField(db_column='Smena', blank=True, null=True)  # Field name made lowercase.
    ncheck = models.IntegerField(db_column='NCheck', blank=True, null=True)  # Field name made lowercase.
    nalin = models.DecimalField(db_column='NalIn', max_digits=18, decimal_places=2, blank=True,
                                null=True)  # Field name made lowercase.
    beznalin = models.DecimalField(db_column='BeznalIn', max_digits=18, decimal_places=2, blank=True,
                                   null=True)  # Field name made lowercase.
    nalout = models.DecimalField(db_column='NalOut', max_digits=18, decimal_places=2, blank=True,
                                 null=True)  # Field name made lowercase.
    beznalout = models.DecimalField(db_column='BeznalOut', max_digits=18, decimal_places=2, blank=True,
                                    null=True)  # Field name made lowercase.
    vnes = models.DecimalField(db_column='Vnes', max_digits=18, decimal_places=2, blank=True,
                               null=True)  # Field name made lowercase.
    vines = models.DecimalField(db_column='Vines', max_digits=18, decimal_places=2, blank=True,
                                null=True)  # Field name made lowercase.
    computername = models.DecimalField(db_column='ComputerName', max_digits=18, decimal_places=2, blank=True,
                                       null=True)  # Field name made lowercase.
    main = models.BooleanField(db_column='Main', blank=True, null=True)  # Field name made lowercase.
    extendeddata = models.TextField(db_column='ExtendedData', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Kkm'


class Kursovka(models.Model):
    kursovkaid = models.AutoField(db_column='KursovkaId', primary_key=True)  # Field name made lowercase.
    superaccountid = models.ForeignKey('Superaccount', models.DO_NOTHING,
                                       db_column='SuperAccountId')  # Field name made lowercase.
    start = models.DateTimeField(db_column='Start')  # Field name made lowercase.
    end = models.DateTimeField(db_column='End')  # Field name made lowercase.
    series = models.CharField(db_column='Series', max_length=20, blank=True, null=True)  # Field name made lowercase.
    number = models.IntegerField(db_column='Number', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Kursovka'


class Kursovkadetail(models.Model):
    kursovkadetailid = models.AutoField(db_column='KursovkaDetailId', primary_key=True)  # Field name made lowercase.
    kursovkaid = models.ForeignKey(Kursovka, models.DO_NOTHING, db_column='KursovkaId')  # Field name made lowercase.
    accountstockid = models.ForeignKey(Accountstock, models.DO_NOTHING,
                                       db_column='AccountStockId')  # Field name made lowercase.
    returntime = models.DateTimeField(db_column='ReturnTime', blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=18, decimal_places=2, blank=True,
                               null=True)  # Field name made lowercase.
    returncost = models.DecimalField(db_column='ReturnCost', max_digits=18, decimal_places=2, blank=True,
                                     null=True)  # Field name made lowercase.
    returnservicepointid = models.ForeignKey('Servicepoint', models.DO_NOTHING, db_column='ReturnServicePointId',
                                             related_name='returnservicepointid', blank=True,
                                             null=True)  # Field name made lowercase.
    sellservicepointid = models.ForeignKey('Servicepoint', models.DO_NOTHING, db_column='SellServicePointId',
                                           related_name='sellservicepointid', blank=True,
                                           null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KursovkaDetail'


class Leaseorder(models.Model):
    leaseorderid = models.AutoField(db_column='LeaseOrderId', primary_key=True)  # Field name made lowercase.
    superaccountid = models.ForeignKey('Superaccount', models.DO_NOTHING,
                                       db_column='SuperAccountId')  # Field name made lowercase.
    closed = models.BooleanField(db_column='Closed')  # Field name made lowercase.
    closetime = models.DateTimeField(db_column='CloseTime', blank=True, null=True)  # Field name made lowercase.
    openservicepointid = models.ForeignKey('Servicepoint', models.DO_NOTHING, db_column='OpenServicePointId',
                                           related_name='openservicepointid', blank=True,
                                           null=True)  # Field name made lowercase.
    closeservicepointid = models.ForeignKey('Servicepoint', models.DO_NOTHING, db_column='CloseServicePointId',
                                            related_name='closeservicepointid', blank=True,
                                            null=True)  # Field name made lowercase.
    opentime = models.DateTimeField(db_column='OpenTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LeaseOrder'


class Lookupinterface(models.Model):
    lookupinterfaceid = models.IntegerField(db_column='LookupInterfaceId',
                                            primary_key=True)  # Field name made lowercase.
    parentid = models.IntegerField(db_column='ParentId')  # Field name made lowercase.
    viewstring = models.CharField(db_column='ViewString', max_length=100)  # Field name made lowercase.
    isfolder = models.BooleanField(db_column='IsFolder')  # Field name made lowercase.
    lookuplink = models.BigIntegerField(db_column='LookupLink', blank=True, null=True)  # Field name made lowercase.
    lookuptype = models.SmallIntegerField(db_column='LookupType')  # Field name made lowercase.
    extendeddata = models.TextField(db_column='ExtendedData', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LookupInterface'


class Mastertransaction(models.Model):
    mastertransactionid = models.AutoField(db_column='MasterTransactionId',
                                           primary_key=True)  # Field name made lowercase.
    transtime = models.DateTimeField(db_column='TransTime')  # Field name made lowercase.
    superaccountfrom = models.ForeignKey('Superaccount', models.DO_NOTHING, db_column='SuperAccountFrom',
                                         related_name='superaccountfrom', blank=True,
                                         null=True)  # Field name made lowercase.
    superaccountto = models.ForeignKey('Superaccount', models.DO_NOTHING, db_column='SuperAccountTo',
                                       related_name='superaccountto', blank=True,
                                       null=True)  # Field name made lowercase.
    userid = models.CharField(db_column='UserId', max_length=50)  # Field name made lowercase.
    geographyid = models.ForeignKey(Geography, models.DO_NOTHING, db_column='GeographyId', blank=True,
                                    null=True)  # Field name made lowercase.
    servicepointid = models.IntegerField(db_column='ServicePointId', blank=True,
                                         null=True)  # Field name made lowercase.
    servertime = models.DateTimeField(db_column='ServerTime', blank=True, null=True)  # Field name made lowercase.
    isoffline = models.BooleanField(db_column='IsOffline')  # Field name made lowercase.
    checkdetailid = models.ForeignKey(Checkdetail, models.DO_NOTHING, db_column='CheckDetailId', blank=True,
                                      null=True)  # Field name made lowercase.
    extendeddata = models.TextField(db_column='ExtendedData', blank=True, null=True)  # Field name made lowercase.
    externalid = models.CharField(db_column='ExternalId', max_length=50, blank=True,
                                  null=True)  # Field name made lowercase.
    hash = models.CharField(db_column='Hash', max_length=50, blank=True, null=True)  # Field name made lowercase.
    machine = models.CharField(db_column='Machine', max_length=50, blank=True, null=True)  # Field name made lowercase.
    secsubjectid = models.ForeignKey('Secsubject', models.DO_NOTHING, db_column='SecSubjectId', blank=True,
                                     null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MasterTransaction'


class Module(models.Model):
    moduleid = models.CharField(db_column='ModuleId', primary_key=True, max_length=50)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    machinename = models.CharField(db_column='MachineName', max_length=50, blank=True,
                                   null=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.DateTimeField(db_column='LastUpdate', blank=True, null=True)  # Field name made lowercase.
    localconfig = models.TextField(db_column='LocalConfig', blank=True, null=True)  # Field name made lowercase.
    extendeddata = models.TextField(db_column='ExtendedData', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Module'


class Moneypledgedetail(models.Model):
    moneypledgedetailid = models.IntegerField(db_column='MoneyPledgeDetailId',
                                              primary_key=True)  # Field name made lowercase.
    ownerid = models.ForeignKey(Accountstock, models.DO_NOTHING, db_column='OwnerId')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=18, decimal_places=2)  # Field name made lowercase.
    targetaccountstockid = models.IntegerField(db_column='TargetAccountStockId')  # Field name made lowercase.
    taketime = models.DateTimeField(db_column='TakeTime')  # Field name made lowercase.
    returntime = models.DateTimeField(db_column='ReturnTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MoneyPledgeDetail'


class Number(models.Model):
    number = models.IntegerField(db_column='Number', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Number'


class Order(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    returnorderid = models.CharField(db_column='ReturnOrderId', max_length=64, blank=True,
                                     null=True)  # Field name made lowercase.
    bankorderid = models.CharField(db_column='BankOrderId', max_length=64, blank=True,
                                   null=True)  # Field name made lowercase.
    superaccountid = models.ForeignKey('Superaccount', models.DO_NOTHING,
                                       db_column='SuperAccountId')  # Field name made lowercase.
    siteid = models.IntegerField(db_column='SiteId', blank=True, null=True)  # Field name made lowercase.
    profileid = models.IntegerField(db_column='ProfileId', blank=True, null=True)  # Field name made lowercase.
    merchantid = models.IntegerField(db_column='MerchantId', blank=True, null=True)  # Field name made lowercase.
    addbalanceamount = models.DecimalField(db_column='AddBalanceAmount', max_digits=19, decimal_places=4, blank=True,
                                           null=True)  # Field name made lowercase.
    customproperty = models.CharField(db_column='CustomProperty', max_length=2000, blank=True,
                                      null=True)  # Field name made lowercase.
    appkey = models.CharField(db_column='AppKey', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Order'


class Ordercheck(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    ownerid = models.IntegerField(db_column='OwnerId', blank=True, null=True)  # Field name made lowercase.
    idcategory = models.IntegerField(db_column='IdCategory', blank=True, null=True)  # Field name made lowercase.
    codecard = models.CharField(db_column='CodeCard', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    linked = models.BooleanField(db_column='Linked', blank=True, null=True)  # Field name made lowercase.
    from_field = models.DateTimeField(db_column='From', blank=True,
                                      null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    to = models.DateTimeField(db_column='To', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    amountminutes = models.IntegerField(db_column='AmountMinutes', blank=True, null=True)  # Field name made lowercase.
    idmediatype = models.IntegerField(db_column='IdMediaType', blank=True, null=True)  # Field name made lowercase.
    cardname = models.CharField(db_column='CardName', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    typegoods = models.SmallIntegerField(db_column='TypeGoods', blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=18, decimal_places=2, blank=True,
                                null=True)  # Field name made lowercase.
    firstcode = models.CharField(db_column='FirstCode', max_length=50, blank=True,
                                 null=True)  # Field name made lowercase.
    firstclientid = models.IntegerField(db_column='FirstClientId', blank=True, null=True)  # Field name made lowercase.
    dopinfo = models.TextField(db_column='DopInfo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OrderCheck'


class Orderdetail(models.Model):
    orderdetailid = models.IntegerField(db_column='OrderDetailId', primary_key=True)  # Field name made lowercase.
    orderid = models.IntegerField(db_column='OrderId')  # Field name made lowercase.
    inventoryid = models.ForeignKey(Accountstock, models.DO_NOTHING,
                                    db_column='InventoryId')  # Field name made lowercase.
    giveouttime = models.DateTimeField(db_column='GiveOutTime')  # Field name made lowercase.
    returntime = models.DateTimeField(db_column='ReturnTime', blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=18, decimal_places=2, blank=True,
                               null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OrderDetail'


class Orderstatus(models.Model):
    orderid = models.OneToOneField(Order, models.DO_NOTHING, db_column='OrderId',
                                   primary_key=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status')  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='TimeStamp')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OrderStatus'
        unique_together = (('orderid', 'status'),)


class Packetdetail(models.Model):
    packetdetailid = models.AutoField(db_column='PacketDetailId', primary_key=True)  # Field name made lowercase.
    accountstockid = models.ForeignKey(Accountstock, models.DO_NOTHING, db_column='AccountStockId',
                                       related_name='packetdetailaccountstockid')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=18, decimal_places=2)  # Field name made lowercase.
    packetid = models.ForeignKey(Accountstock, models.DO_NOTHING, db_column='PacketId',
                                 related_name='packetid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PacketDetail'


class Permission(models.Model):
    subjectid = models.ForeignKey('Secsubject', models.DO_NOTHING, db_column='SubjectID')  # Field name made lowercase.
    objectid = models.ForeignKey('Secobject', models.DO_NOTHING, db_column='ObjectID')  # Field name made lowercase.
    accesscode = models.BooleanField(db_column='AccessCode')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Permission'
        unique_together = (('subjectid', 'objectid'),)


class Personalinfo(models.Model):
    firstname = models.CharField(db_column='FirstName', max_length=50, blank=True,
                                 null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    secondname = models.CharField(db_column='SecondName', max_length=50, blank=True,
                                  null=True)  # Field name made lowercase.
    info = models.TextField(db_column='Info', blank=True, null=True)  # Field name made lowercase.
    weight = models.IntegerField(db_column='Weight', blank=True, null=True)  # Field name made lowercase.
    height = models.IntegerField(db_column='Height', blank=True, null=True)  # Field name made lowercase.
    feetsize = models.IntegerField(db_column='FeetSize', blank=True, null=True)  # Field name made lowercase.
    passport = models.CharField(db_column='Passport', max_length=100, blank=True,
                                null=True)  # Field name made lowercase.
    drivinglicence = models.CharField(db_column='DrivingLicence', max_length=100, blank=True,
                                      null=True)  # Field name made lowercase.
    armypassport = models.CharField(db_column='ArmyPassport', max_length=100, blank=True,
                                    null=True)  # Field name made lowercase.
    document = models.CharField(db_column='Document', max_length=100, blank=True,
                                null=True)  # Field name made lowercase.
    isvip = models.BooleanField(db_column='IsVip')  # Field name made lowercase.
    accountstockid = models.IntegerField(db_column='AccountStockId', primary_key=True)  # Field name made lowercase.
    superaccountid = models.ForeignKey('Superaccount', models.DO_NOTHING,
                                       db_column='SuperAccountId')  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=100, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    birthday = models.DateTimeField(db_column='Birthday', blank=True, null=True)  # Field name made lowercase.
    passwordhash = models.CharField(db_column='PasswordHash', max_length=100, blank=True,
                                    null=True)  # Field name made lowercase.
    ispasswordchangerequired = models.BooleanField(db_column='IsPasswordChangeRequired')  # Field name made lowercase.
    passportcode = models.CharField(db_column='PassportCode', max_length=50, blank=True,
                                    null=True)  # Field name made lowercase.
    drivinglicencecode = models.CharField(db_column='DrivingLicenceCode', max_length=50, blank=True,
                                          null=True)  # Field name made lowercase.
    tempemail = models.CharField(db_column='TempEmail', max_length=50, blank=True,
                                 null=True)  # Field name made lowercase.
    tempphone = models.CharField(db_column='TempPhone', max_length=50, blank=True,
                                 null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PersonalInfo'


class Place(models.Model):
    placeid = models.AutoField(db_column='PlaceId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    parentid = models.IntegerField(db_column='ParentId', blank=True, null=True)  # Field name made lowercase.
    depth = models.IntegerField(db_column='Depth', blank=True, null=True)  # Field name made lowercase.
    allowintersectschedules = models.BooleanField(db_column='AllowIntersectSchedules')  # Field name made lowercase.
    placetypeid = models.ForeignKey('Placetype', models.DO_NOTHING, db_column='PlaceTypeId', blank=True,
                                    null=True)  # Field name made lowercase.
    attribute = models.CharField(db_column='Attribute', max_length=50, blank=True,
                                 null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Place'


class Placereserve(models.Model):
    placereserveid = models.AutoField(db_column='PlaceReserveId', primary_key=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True,
                                   null=True)  # Field name made lowercase.
    externalsellerid = models.ForeignKey(Externalseller, models.DO_NOTHING, db_column='ExternalSellerId', blank=True,
                                         null=True)  # Field name made lowercase.
    reservetime = models.DateTimeField(db_column='ReserveTime', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    explicitexpirationtime = models.DateTimeField(db_column='ExplicitExpirationTime', blank=True,
                                                  null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PlaceReserve'


class Placescheme(models.Model):
    placeschemeid = models.AutoField(db_column='PlaceSchemeId', primary_key=True)  # Field name made lowercase.
    schemeobjecttype = models.IntegerField(db_column='SchemeObjectType')  # Field name made lowercase.
    placeid = models.ForeignKey(Place, models.DO_NOTHING, db_column='PlaceId', blank=True,
                                null=True)  # Field name made lowercase.
    idlabel = models.CharField(db_column='IdLabel', max_length=50, blank=True, null=True)  # Field name made lowercase.
    parentplaceschemeid = models.ForeignKey('self', models.DO_NOTHING, db_column='ParentPlaceSchemeId', blank=True,
                                            null=True)  # Field name made lowercase.
    layer = models.IntegerField(db_column='Layer')  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='TimeStamp')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PlaceScheme'


class Placetype(models.Model):
    placetypeid = models.AutoField(db_column='PlaceTypeId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nameforweb = models.CharField(db_column='NameForWeb', max_length=50, blank=True,
                                  null=True)  # Field name made lowercase.
    freecolor = models.IntegerField(db_column='FreeColor', blank=True, null=True)  # Field name made lowercase.
    bookedcolor = models.IntegerField(db_column='BookedColor', blank=True, null=True)  # Field name made lowercase.
    reservedcolor = models.IntegerField(db_column='ReservedColor', blank=True, null=True)  # Field name made lowercase.
    reservedcurrentcolor = models.IntegerField(db_column='ReservedCurrentColor', blank=True,
                                               null=True)  # Field name made lowercase.
    selectedcolor = models.IntegerField(db_column='SelectedColor', blank=True, null=True)  # Field name made lowercase.
    selectedcurrentcolor = models.IntegerField(db_column='SelectedCurrentColor', blank=True,
                                               null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PlaceType'


class Pledge(models.Model):
    pledgeid = models.IntegerField(db_column='PledgeId', primary_key=True)  # Field name made lowercase.
    descr = models.CharField(db_column='Descr', max_length=1024)  # Field name made lowercase.
    exist = models.BooleanField(db_column='Exist')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pledge'


class Prepay(models.Model):
    prepayid = models.IntegerField(db_column='PrepayId', primary_key=True)  # Field name made lowercase.
    currencyid = models.IntegerField(db_column='CurrencyId')  # Field name made lowercase.
    balance = models.DecimalField(db_column='Balance', max_digits=18, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Prepay'


class Price(models.Model):
    priceid = models.IntegerField(db_column='PriceId', primary_key=True)  # Field name made lowercase.
    timingintervalid = models.ForeignKey('Timinginterval', models.DO_NOTHING,
                                         db_column='TimingIntervalId')  # Field name made lowercase.
    tariffid = models.ForeignKey('Tariff', models.DO_NOTHING, db_column='TariffId')  # Field name made lowercase.
    allow = models.BooleanField(db_column='Allow')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=18, decimal_places=2)  # Field name made lowercase.
    min = models.DecimalField(db_column='Min', max_digits=18, decimal_places=2)  # Field name made lowercase.
    max = models.DecimalField(db_column='Max', max_digits=18, decimal_places=2)  # Field name made lowercase.
    round = models.IntegerField(db_column='Round')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Price'


class Priceparams(models.Model):
    priceparamsid = models.IntegerField(db_column='PriceParamsId', primary_key=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=18, decimal_places=2)  # Field name made lowercase.
    maxprice = models.DecimalField(db_column='MaxPrice', max_digits=18, decimal_places=2)  # Field name made lowercase.
    minprice = models.DecimalField(db_column='MinPrice', max_digits=18, decimal_places=2)  # Field name made lowercase.
    rounddigits = models.IntegerField(db_column='RoundDigits')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PriceParams'


class Reader(models.Model):
    readerid = models.IntegerField(db_column='ReaderId', primary_key=True)  # Field name made lowercase.
    code = models.IntegerField(db_column='Code')  # Field name made lowercase.
    controllerid = models.ForeignKey(Controller, models.DO_NOTHING,
                                     db_column='ControllerId')  # Field name made lowercase.
    facilityid = models.IntegerField(db_column='FacilityId', blank=True, null=True)  # Field name made lowercase.
    timedelay = models.FloatField(db_column='TimeDelay')  # Field name made lowercase.
    regime = models.SmallIntegerField(db_column='Regime', blank=True, null=True)  # Field name made lowercase.
    entry = models.SmallIntegerField(db_column='Entry')  # Field name made lowercase.
    use = models.SmallIntegerField(db_column='Use')  # Field name made lowercase.
    denywithinventory = models.BooleanField(db_column='DenyWithInventory')  # Field name made lowercase.
    denywithoutstoredpledge = models.BooleanField(db_column='DenyWithoutStoredPledge')  # Field name made lowercase.
    geographyid = models.ForeignKey(Geography, models.DO_NOTHING, db_column='GeographyId', blank=True,
                                    null=True)  # Field name made lowercase.
    codeconvert = models.IntegerField(db_column='CodeConvert')  # Field name made lowercase.
    denywithdebt = models.BooleanField(db_column='DenyWithDebt')  # Field name made lowercase.
    closeclientaccount = models.BooleanField(db_column='CloseClientAccount')  # Field name made lowercase.
    directioncode = models.IntegerField(db_column='DirectionCode')  # Field name made lowercase.
    extendeddata = models.TextField(db_column='ExtendedData', blank=True, null=True)  # Field name made lowercase.
    cashid = models.IntegerField(db_column='CashID', blank=True, null=True)  # Field name made lowercase.
    mediaid = models.IntegerField(db_column='MediaID', blank=True, null=True)  # Field name made lowercase.
    disablecheckendpass = models.BooleanField(db_column='DisableCheckEndPass')  # Field name made lowercase.
    facilitypassid = models.IntegerField(db_column='FacilityPassID', blank=True,
                                         null=True)  # Field name made lowercase.
    facilitytype = models.BooleanField(db_column='FacilityType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Reader'


class Reservationorder(models.Model):
    reservationorderid = models.AutoField(db_column='ReservationOrderId',
                                          primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=50, blank=True, null=True)  # Field name made lowercase.
    superaccountid = models.IntegerField(db_column='SuperAccountId', blank=True,
                                         null=True)  # Field name made lowercase.
    storageplacenumber = models.IntegerField(db_column='StoragePlaceNumber', blank=True,
                                             null=True)  # Field name made lowercase.
    datefrom = models.DateTimeField(db_column='DateFrom', blank=True, null=True)  # Field name made lowercase.
    dateto = models.DateTimeField(db_column='DateTo', blank=True, null=True)  # Field name made lowercase.
    registrationdate = models.DateTimeField(db_column='RegistrationDate', blank=True,
                                            null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.
    clientdescription = models.CharField(db_column='ClientDescription', max_length=100, blank=True,
                                         null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReservationOrder'


class Rule(models.Model):
    ruleid = models.AutoField(db_column='RuleId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ruleraw = models.TextField(db_column='RuleRaw', blank=True,
                               null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Rule'


class Schedule(models.Model):
    scheduleid = models.IntegerField(db_column='ScheduleId', primary_key=True)  # Field name made lowercase.
    scheduletype = models.BooleanField(db_column='ScheduleType')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Schedule'


class Seasontemplate(models.Model):
    seasontemplateid = models.AutoField(db_column='SeasonTemplateId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True,
                                   null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SeasonTemplate'


class Seasontemplatedetail(models.Model):
    seasontemplateid = models.OneToOneField(Seasontemplate, models.DO_NOTHING, db_column='SeasonTemplateId',
                                            primary_key=True)  # Field name made lowercase.
    activityscheduleid = models.ForeignKey(Activityschedule, models.DO_NOTHING,
                                           db_column='ActivityScheduleId')  # Field name made lowercase.
    isdefault = models.BooleanField(db_column='IsDefault')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SeasonTemplateDetail'
        unique_together = (('seasontemplateid', 'activityscheduleid'),)


class Secobject(models.Model):
    objectid = models.AutoField(db_column='ObjectID', primary_key=True)  # Field name made lowercase.
    objectkey = models.CharField(db_column='ObjectKey', unique=True, max_length=200)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    group = models.CharField(db_column='Group', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SecObject'


class Secsubject(models.Model):
    subjectid = models.AutoField(db_column='SubjectID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=50)  # Field name made lowercase.
    isgroup = models.BooleanField(db_column='IsGroup')  # Field name made lowercase.
    pwdhash = models.CharField(db_column='PwdHash', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cardhash = models.CharField(db_column='CardHash', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    isembedded = models.BooleanField(db_column='IsEmbedded')  # Field name made lowercase.
    blocked = models.BooleanField(db_column='Blocked', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SecSubject'


class Servicepoint(models.Model):
    servicepointid = models.AutoField(db_column='ServicePointId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    superaccountid = models.ForeignKey('Superaccount', models.DO_NOTHING,
                                       db_column='SuperAccountId')  # Field name made lowercase.
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=20, blank=True, null=True)  # Field name made lowercase.
    isinternal = models.BooleanField(db_column='IsInternal')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ServicePoint'


class Servicepointinfo(models.Model):
    servicepointid = models.ForeignKey(Servicepoint, models.DO_NOTHING,
                                       db_column='ServicePointId')  # Field name made lowercase.
    servicepointtype = models.IntegerField(db_column='ServicePointType')  # Field name made lowercase.
    stockinfoid = models.ForeignKey(Accountstock, models.DO_NOTHING,
                                    db_column='StockInfoId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ServicePointInfo'
        unique_together = (('servicepointid', 'servicepointtype', 'stockinfoid'),)


class Shablonscardprinter(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    extendeddata = models.TextField(db_column='ExtendedData', blank=True, null=True)  # Field name made lowercase.
    shablontype = models.SmallIntegerField(db_column='ShablonType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ShablonsCardPrinter'


class Stafftosubdivision(models.Model):
    superaccountid = models.ForeignKey('Superaccount', models.DO_NOTHING,
                                       db_column='SuperAccountId')  # Field name made lowercase.
    subdivisionid = models.ForeignKey('Subdivision', models.DO_NOTHING,
                                      db_column='SubdivisionId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StaffToSubdivision'


class Stocktype(models.Model):
    stocktype = models.SmallIntegerField(db_column='StockType', primary_key=True)  # Field name made lowercase.
    caption = models.CharField(db_column='Caption', max_length=50)  # Field name made lowercase.
    iscategory = models.BooleanField(db_column='IsCategory')  # Field name made lowercase.
    isgood = models.BooleanField(db_column='IsGood')  # Field name made lowercase.
    ispay = models.BooleanField(db_column='IsPay')  # Field name made lowercase.
    iscount = models.BooleanField(db_column='IsCount')  # Field name made lowercase.
    istime = models.BooleanField(db_column='IsTime')  # Field name made lowercase.
    isdepricated = models.BooleanField(db_column='IsDepricated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StockType'


class Storage(models.Model):
    key = models.CharField(db_column='Key', primary_key=True, max_length=100)  # Field name made lowercase.
    object = models.TextField(db_column='Object', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Storage'


class Storedpledge(models.Model):
    superaccountid = models.ForeignKey('Superaccount', models.DO_NOTHING,
                                       db_column='SuperAccountId')  # Field name made lowercase.
    gettime = models.DateTimeField(db_column='GetTime', blank=True, null=True)  # Field name made lowercase.
    returntime = models.DateTimeField(db_column='ReturnTime', blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase.
    cellnumber = models.IntegerField(db_column='CellNumber')  # Field name made lowercase.
    getuserid = models.ForeignKey(Secsubject, models.DO_NOTHING, db_column='GetUserId', related_name='getuserid',
                                  blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=100, blank=True, null=True)  # Field name made lowercase.
    returnuserid = models.ForeignKey(Secsubject, models.DO_NOTHING, db_column='ReturnUserId',
                                     related_name='returnuserid', blank=True, null=True)  # Field name made lowercase.
    storedpledgeid = models.AutoField(db_column='StoredPledgeId', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StoredPledge'


class Strictticketreel(models.Model):
    strictticketreelid = models.AutoField(db_column='StrictTicketReelId',
                                          primary_key=True)  # Field name made lowercase.
    set = models.CharField(db_column='Set', max_length=5)  # Field name made lowercase.
    start = models.IntegerField(db_column='Start')  # Field name made lowercase.
    step = models.IntegerField(db_column='Step')  # Field name made lowercase.
    count = models.IntegerField(db_column='Count')  # Field name made lowercase.
    position = models.IntegerField(db_column='Position')  # Field name made lowercase.
    ownerid = models.ForeignKey(Secsubject, models.DO_NOTHING, db_column='OwnerId')  # Field name made lowercase.
    usestation = models.CharField(db_column='UseStation', max_length=50, blank=True,
                                  null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StrictTicketReel'


class Subdivision(models.Model):
    subdivisionid = models.AutoField(db_column='SubdivisionId', primary_key=True)  # Field name made lowercase.
    superaccountid = models.ForeignKey('Superaccount', models.DO_NOTHING,
                                       db_column='SuperAccountId')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Subdivision'


class Superaccount(models.Model):
    superaccountid = models.IntegerField(db_column='SuperAccountId', primary_key=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.
    descr = models.CharField(db_column='Descr', max_length=50, blank=True, null=True)  # Field name made lowercase.
    canregister = models.DateTimeField(db_column='CanRegister')  # Field name made lowercase.
    canpass = models.DateTimeField(db_column='CanPass')  # Field name made lowercase.
    isstuff = models.BooleanField(db_column='IsStuff')  # Field name made lowercase.
    isblocked = models.BooleanField(db_column='IsBlocked')  # Field name made lowercase.
    blockreason = models.CharField(db_column='BlockReason', max_length=100, blank=True,
                                   null=True)  # Field name made lowercase.
    denyreturn = models.BooleanField(db_column='DenyReturn')  # Field name made lowercase.
    clientcategoryid = models.ForeignKey(Clientcategory, models.DO_NOTHING, db_column='ClientCategoryId', blank=True,
                                         null=True)  # Field name made lowercase.
    discountcard = models.BooleanField(db_column='DiscountCard')  # Field name made lowercase.
    personalinfoid = models.ForeignKey(Personalinfo, models.DO_NOTHING, db_column='PersonalInfoId', blank=True,
                                       null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=50, blank=True, null=True)  # Field name made lowercase.
    inn = models.CharField(db_column='Inn', max_length=15, blank=True, null=True)  # Field name made lowercase.
    externalid = models.CharField(db_column='ExternalId', max_length=50, blank=True,
                                  null=True)  # Field name made lowercase.
    registertime = models.DateTimeField(db_column='RegisterTime')  # Field name made lowercase.
    lasttransactiontime = models.DateTimeField(db_column='LastTransactionTime')  # Field name made lowercase.
    legalentityrelationtypeid = models.ForeignKey('Superaccountrelationtype', models.DO_NOTHING,
                                                  db_column='LegalEntityRelationTypeId', blank=True,
                                                  null=True)  # Field name made lowercase.
    sellservicepointid = models.ForeignKey(Servicepoint, models.DO_NOTHING, db_column='SellServicePointId',
                                           related_name='superaccountsell', blank=True,
                                           null=True)  # Field name made lowercase.
    depositservicepointid = models.ForeignKey(Servicepoint, models.DO_NOTHING, db_column='DepositServicePointId',
                                              related_name='superaccountdeposit', blank=True,
                                              null=True)  # Field name made lowercase.
    allowignorestoredpledge = models.BooleanField(db_column='AllowIgnoreStoredPledge')  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    latitude = models.DecimalField(db_column='Latitude', max_digits=10, decimal_places=6, blank=True,
                                   null=True)  # Field name made lowercase.
    longitude = models.DecimalField(db_column='Longitude', max_digits=10, decimal_places=6, blank=True,
                                    null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    website = models.CharField(db_column='WebSite', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tng_profileid = models.CharField(db_column='TNG_ProfileId', max_length=50, blank=True,
                                     null=True)  # Field name made lowercase.
    colary_profileid = models.CharField(db_column='Colary_ProfileId', max_length=50, blank=True,
                                        null=True)  # Field name made lowercase.
    tng_profileverified = models.BooleanField(db_column='TNG_ProfileVerified')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SuperAccount'


class Superaccountclaim(models.Model):
    superaccountid = models.ForeignKey(Superaccount, models.DO_NOTHING,
                                       db_column='SuperAccountId')  # Field name made lowercase.
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=50)  # Field name made lowercase.
    expirationdate = models.DateTimeField(db_column='ExpirationDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SuperAccountClaim'


class Superaccountrelation(models.Model):
    parentsuperaccountid = models.ForeignKey(Superaccount, models.DO_NOTHING, db_column='ParentSuperAccountId',
                                             related_name='superaccountrelationparent')  # Field name made lowercase.
    slavesuperaccountid = models.ForeignKey(Superaccount, models.DO_NOTHING, db_column='SlaveSuperAccountId',
                                            related_name='superaccountrelationslave')  # Field name made lowercase.
    userid = models.ForeignKey(Secsubject, models.DO_NOTHING, db_column='UserId')  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=100, blank=True, null=True)  # Field name made lowercase.
    superaccountrelationtypeid = models.ForeignKey('Superaccountrelationtype', models.DO_NOTHING,
                                                   db_column='SuperAccountRelationTypeId')  # Field name made lowercase.
    extendeddata = models.TextField(db_column='ExtendedData', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SuperAccountRelation'
        unique_together = (('parentsuperaccountid', 'slavesuperaccountid', 'superaccountrelationtypeid'),)


class Superaccountrelationtype(models.Model):
    superaccountrelationtypeid = models.AutoField(db_column='SuperAccountRelationTypeId',
                                                  primary_key=True)  # Field name made lowercase.
    parentname = models.CharField(db_column='ParentName', max_length=50)  # Field name made lowercase.
    slavename = models.CharField(db_column='SlaveName', max_length=50)  # Field name made lowercase.
    parenttagid = models.ForeignKey('Tag', models.DO_NOTHING, db_column='ParentTagId',
                                    related_name='superaccountrelationtypeparent', blank=True,
                                    null=True)  # Field name made lowercase.
    parenttaginheritance = models.IntegerField(db_column='ParentTagInheritance', blank=True,
                                               null=True)  # Field name made lowercase.
    slavetagid = models.ForeignKey('Tag', models.DO_NOTHING, db_column='SlaveTagId',
                                   related_name='superaccountrelationtypeslave', blank=True,
                                   null=True)  # Field name made lowercase.
    extendeddata = models.TextField(db_column='ExtendedData', blank=True, null=True)  # Field name made lowercase.
    allowuseparentmoney = models.BooleanField(db_column='AllowUseParentMoney')  # Field name made lowercase.
    allowuseparentstoredpledge = models.BooleanField(
        db_column='AllowUseParentStoredPledge')  # Field name made lowercase.
    deleteonparentreturnstoredpledge = models.BooleanField(
        db_column='DeleteOnParentReturnStoredPledge')  # Field name made lowercase.
    adminonly = models.BooleanField(db_column='AdminOnly')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SuperAccountRelationType'


class Superaccounttimestop(models.Model):
    superaccounttimestopid = models.AutoField(db_column='SuperAccountTimeStopId',
                                              primary_key=True)  # Field name made lowercase.
    superaccountid = models.ForeignKey(Superaccount, models.DO_NOTHING,
                                       db_column='SuperAccountId')  # Field name made lowercase.
    scope = models.IntegerField(db_column='Scope')  # Field name made lowercase.
    targettype = models.SmallIntegerField(db_column='TargetType')  # Field name made lowercase.
    categoryid = models.ForeignKey(Category, models.DO_NOTHING, db_column='CategoryId', blank=True,
                                   null=True)  # Field name made lowercase.
    from_field = models.DateTimeField(
        db_column='From')  # Field name made lowercase. Field renamed because it was a Python reserved word.
    to = models.DateTimeField(db_column='To', blank=True, null=True)  # Field name made lowercase.
    fromreaderid = models.ForeignKey(Reader, models.DO_NOTHING, db_column='FromReaderId',
                                     related_name='superaccounttimestopfrom', blank=True,
                                     null=True)  # Field name made lowercase.
    toreaderid = models.ForeignKey(Reader, models.DO_NOTHING, db_column='ToReaderId',
                                   related_name='superaccounttimestopto', blank=True,
                                   null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SuperAccountTimeStop'


class Tag(models.Model):
    tagid = models.AutoField(db_column='TagId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tag'


class Tariff(models.Model):
    tariffid = models.IntegerField(db_column='TariffId', primary_key=True)  # Field name made lowercase.
    targetgoodid = models.ForeignKey(Category, models.DO_NOTHING, db_column='TargetGoodId',
                                     related_name='tariffpaytargetgood')  # Field name made lowercase.
    targetgoodtype = models.SmallIntegerField(db_column='TargetGoodType')  # Field name made lowercase.
    payrightid = models.ForeignKey(Category, models.DO_NOTHING, db_column='PayRightId', related_name='tariffpayright',
                                   blank=True, null=True)  # Field name made lowercase.
    payrighttype = models.SmallIntegerField(db_column='PayRightType')  # Field name made lowercase.
    dependence = models.IntegerField(db_column='Dependence')  # Field name made lowercase.
    timingscheduletime = models.SmallIntegerField(db_column='TimingScheduleTime')  # Field name made lowercase.
    extendeddata = models.TextField(db_column='ExtendedData', blank=True, null=True)  # Field name made lowercase.
    paybybooking = models.IntegerField(db_column='PayByBooking')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tariff'


class Tariffextension(models.Model):
    tariffextensionid = models.IntegerField(db_column='TariffExtensionId',
                                            primary_key=True)  # Field name made lowercase.
    tariffid = models.ForeignKey(Tariff, models.DO_NOTHING, db_column='TariffId', blank=True,
                                 null=True)  # Field name made lowercase.
    scheduleid = models.ForeignKey(Schedule, models.DO_NOTHING, db_column='ScheduleId', blank=True,
                                   null=True)  # Field name made lowercase.
    daytypeid = models.ForeignKey(Daytype, models.DO_NOTHING, db_column='DayTypeId', blank=True,
                                  null=True)  # Field name made lowercase.
    parenttariffextensionid = models.ForeignKey('self', models.DO_NOTHING, db_column='ParentTariffExtensionId',
                                                blank=True, null=True)  # Field name made lowercase.
    timingintervalid = models.ForeignKey('Timinginterval', models.DO_NOTHING, db_column='TimingIntervalId', blank=True,
                                         null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.
    max = models.DecimalField(db_column='Max', max_digits=18, decimal_places=2, blank=True,
                              null=True)  # Field name made lowercase.
    min = models.DecimalField(db_column='Min', max_digits=18, decimal_places=2, blank=True,
                              null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=18, decimal_places=2, blank=True,
                                 null=True)  # Field name made lowercase.
    round = models.IntegerField(db_column='Round', blank=True, null=True)  # Field name made lowercase.
    allow = models.BooleanField(db_column='Allow', blank=True, null=True)  # Field name made lowercase.
    iscompletepay = models.BooleanField(db_column='IsCompletePay')  # Field name made lowercase.
    orderofpayments = models.IntegerField(db_column='OrderOfPayments')  # Field name made lowercase.
    canaddbonus = models.BooleanField(db_column='CanAddBonus')  # Field name made lowercase.
    number = models.DecimalField(db_column='Number', max_digits=18, decimal_places=2)  # Field name made lowercase.
    tagid = models.ForeignKey(Tag, models.DO_NOTHING, db_column='TagId', blank=True,
                              null=True)  # Field name made lowercase.
    overdraft = models.DecimalField(db_column='Overdraft', max_digits=18,
                                    decimal_places=2)  # Field name made lowercase.
    clientcategoryid = models.ForeignKey(Clientcategory, models.DO_NOTHING, db_column='ClientCategoryId', blank=True,
                                         null=True)  # Field name made lowercase.
    attendantamount = models.IntegerField(db_column='AttendantAmount', blank=True,
                                          null=True)  # Field name made lowercase.
    extendeddata = models.TextField(db_column='ExtendedData', blank=True, null=True)  # Field name made lowercase.
    placetypeid = models.ForeignKey(Placetype, models.DO_NOTHING, db_column='PlaceTypeId', blank=True,
                                    null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TariffExtension'


class Tarifftemplate(models.Model):
    tarifftemplateid = models.AutoField(db_column='TariffTemplateId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    dependence = models.IntegerField(db_column='Dependence')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TariffTemplate'


class Terminallog(models.Model):
    terminalnumber = models.IntegerField(db_column='TerminalNumber')  # Field name made lowercase.
    totalsum = models.DecimalField(db_column='TotalSum', max_digits=18, decimal_places=2)  # Field name made lowercase.
    nominal = models.DecimalField(db_column='Nominal', max_digits=18, decimal_places=2, blank=True,
                                  null=True)  # Field name made lowercase.
    count = models.IntegerField(db_column='Count')  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time')  # Field name made lowercase.
    action = models.IntegerField(db_column='Action')  # Field name made lowercase.
    device = models.IntegerField(db_column='Device')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TerminalLog'


class Timablehold(models.Model):
    timableholdid = models.AutoField(db_column='TimableHoldId', primary_key=True)  # Field name made lowercase.
    from_field = models.DateTimeField(
        db_column='From')  # Field name made lowercase. Field renamed because it was a Python reserved word.
    to = models.DateTimeField(db_column='To')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.
    accountstockid = models.ForeignKey(Accountstock, models.DO_NOTHING,
                                       db_column='AccountStockId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TimableHold'


class Timepattern(models.Model):
    timepatternid = models.AutoField(db_column='TimePatternId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.
    fromdate = models.DateTimeField(db_column='FromDate', blank=True, null=True)  # Field name made lowercase.
    todate = models.DateTimeField(db_column='ToDate', blank=True, null=True)  # Field name made lowercase.
    from_field = models.IntegerField(db_column='From', blank=True,
                                     null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    to = models.IntegerField(db_column='To', blank=True, null=True)  # Field name made lowercase.
    duration = models.IntegerField(db_column='Duration', blank=True, null=True)  # Field name made lowercase.
    activatetype = models.IntegerField(db_column='ActivateType', blank=True, null=True)  # Field name made lowercase.
    canactivatefrom = models.DateTimeField(db_column='CanActivateFrom', blank=True,
                                           null=True)  # Field name made lowercase.
    canactivateto = models.DateTimeField(db_column='CanActivateTo', blank=True, null=True)  # Field name made lowercase.
    daystoactivate = models.IntegerField(db_column='DaysToActivate', blank=True,
                                         null=True)  # Field name made lowercase.
    dayround = models.IntegerField(db_column='DayRound')  # Field name made lowercase.
    startafter = models.IntegerField(db_column='StartAfter')  # Field name made lowercase.
    scheduleid = models.ForeignKey(Schedule, models.DO_NOTHING, db_column='ScheduleId', blank=True,
                                   null=True)  # Field name made lowercase.
    allowedbeforeorafter = models.IntegerField(db_column='AllowedBeforeOrAfter', blank=True,
                                               null=True)  # Field name made lowercase.
    holdsenabled = models.BooleanField(db_column='HoldsEnabled', blank=True, null=True)  # Field name made lowercase.
    maxholddays = models.IntegerField(db_column='MaxHoldDays', blank=True, null=True)  # Field name made lowercase.
    maxholdsnumber = models.IntegerField(db_column='MaxHoldsNumber', blank=True,
                                         null=True)  # Field name made lowercase.
    options = models.TextField(db_column='Options', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TimePattern'


class Timinginterval(models.Model):
    timingintervalid = models.IntegerField(db_column='TimingIntervalId', primary_key=True)  # Field name made lowercase.
    start = models.IntegerField(db_column='Start')  # Field name made lowercase.
    end = models.IntegerField(db_column='End')  # Field name made lowercase.
    step = models.IntegerField(db_column='Step')  # Field name made lowercase.
    delta = models.IntegerField(db_column='Delta')  # Field name made lowercase.
    scheduleid = models.ForeignKey(Schedule, models.DO_NOTHING, db_column='ScheduleId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TimingInterval'


class Timingschedule(models.Model):
    timingscheduleid = models.AutoField(db_column='TimingScheduleId', primary_key=True)  # Field name made lowercase.
    daytypeid = models.ForeignKey(Daytype, models.DO_NOTHING, db_column='DayTypeId', blank=True,
                                  null=True)  # Field name made lowercase.
    timingintervalid = models.ForeignKey(Timinginterval, models.DO_NOTHING, db_column='TimingIntervalId', blank=True,
                                         null=True)  # Field name made lowercase.
    targetid = models.ForeignKey(Accountstock, models.DO_NOTHING, db_column='TargetId')  # Field name made lowercase.
    targettype = models.SmallIntegerField(db_column='TargetType')  # Field name made lowercase.
    data = models.TextField(db_column='Data', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TimingSchedule'


class Transactiondetail(models.Model):
    transactiondetailid = models.AutoField(db_column='TransactionDetailId',
                                           primary_key=True)  # Field name made lowercase.
    mastertransactionid = models.ForeignKey(Mastertransaction, models.DO_NOTHING,
                                            db_column='MasterTransactionId')  # Field name made lowercase.
    stockinfoidfrom = models.ForeignKey(Accountstock, models.DO_NOTHING, db_column='StockInfoIdFrom',
                                        related_name='transactiondetailstockinfofrom', blank=True,
                                        null=True)  # Field name made lowercase.
    stockinfoidto = models.ForeignKey(Accountstock, models.DO_NOTHING, db_column='StockInfoIdTo',
                                      related_name='transactiondetailstockinfoto', blank=True,
                                      null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=18, decimal_places=2)  # Field name made lowercase.
    superaccountidfrom = models.ForeignKey(Superaccount, models.DO_NOTHING, db_column='SuperAccountIdFrom',
                                           related_name='transactiondetailsuperaccountfrom', blank=True,
                                           null=True)  # Field name made lowercase.
    superaccountidto = models.ForeignKey(Superaccount, models.DO_NOTHING, db_column='SuperAccountIdTo',
                                         related_name='transactiondetailsuperaccountto', blank=True,
                                         null=True)  # Field name made lowercase.
    hash = models.CharField(db_column='Hash', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TransactionDetail'


class Transactionprocessingrule(models.Model):
    transactionprocessingruleid = models.AutoField(db_column='TransactionProcessingRuleId',
                                                   primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    from_field = models.DateTimeField(db_column='From', blank=True,
                                      null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    to = models.DateTimeField(db_column='To', blank=True, null=True)  # Field name made lowercase.
    body = models.TextField(db_column='Body', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TransactionProcessingRule'


class Transactionprocessingrulelog(models.Model):
    time = models.DateTimeField(db_column='Time')  # Field name made lowercase.
    transactionprocessingruleid = models.ForeignKey(Transactionprocessingrule, models.DO_NOTHING,
                                                    db_column='TransactionProcessingRuleId')  # Field name made lowercase.
    superaccountid = models.ForeignKey(Superaccount, models.DO_NOTHING,
                                       db_column='SuperAccountId')  # Field name made lowercase.
    mastertransactionid = models.ForeignKey(Mastertransaction, models.DO_NOTHING,
                                            db_column='MasterTransactionId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TransactionProcessingRuleLog'


class Transactionrefinement(models.Model):
    transactionrefinementid = models.AutoField(db_column='TransactionRefinementId',
                                               primary_key=True)  # Field name made lowercase.
    mastertransactionid = models.ForeignKey(Mastertransaction, models.DO_NOTHING,
                                            db_column='MasterTransactionId')  # Field name made lowercase.
    overdraftvolume = models.DecimalField(db_column='OverdraftVolume', max_digits=18, decimal_places=2, blank=True,
                                          null=True)  # Field name made lowercase.
    moneyvolume = models.DecimalField(db_column='MoneyVolume', max_digits=18, decimal_places=2, blank=True,
                                      null=True)  # Field name made lowercase.
    targetstockid = models.ForeignKey(Accountstock, models.DO_NOTHING, db_column='TargetStockId', blank=True,
                                      null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TransactionRefinement'


class User2Groups(models.Model):
    userid = models.ForeignKey(Secsubject, models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    groupid = models.IntegerField(db_column='GroupID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'User2Groups'
        unique_together = (('userid', 'groupid'),)


class Userextension(models.Model):
    userextensionid = models.OneToOneField(Secsubject, models.DO_NOTHING, db_column='UserExtensionId',
                                           primary_key=True)  # Field name made lowercase.
    cashdeskid = models.ForeignKey(Servicepoint, models.DO_NOTHING, db_column='CashDeskId', blank=True,
                                   null=True)  # Field name made lowercase.
    password = models.IntegerField(db_column='Password', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserExtension'


class Usertocategory(models.Model):
    subjectid = models.ForeignKey(Secsubject, models.DO_NOTHING, db_column='SubjectId')  # Field name made lowercase.
    categoryid = models.ForeignKey(Category, models.DO_NOTHING, db_column='CategoryId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserToCategory'
        unique_together = (('subjectid', 'categoryid'),)


class Vatrate(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    vattype = models.IntegerField(db_column='VatType')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rate = models.DecimalField(db_column='Rate', max_digits=18, decimal_places=2, blank=True,
                               null=True)  # Field name made lowercase.
    withoutvat = models.BooleanField(db_column='Withoutvat', blank=True, null=True)  # Field name made lowercase.
    idatol = models.SmallIntegerField(db_column='IdAtol', blank=True, null=True)  # Field name made lowercase.
    idprim = models.SmallIntegerField(db_column='IdPrim', blank=True, null=True)  # Field name made lowercase.
    idshtrih = models.SmallIntegerField(db_column='IdShtrih', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VatRate'
