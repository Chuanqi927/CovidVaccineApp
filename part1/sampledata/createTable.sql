create table prioritygroup
(
    groupNumber  int  not null
        primary key,
    EligibleDate date not null
);

create table patients
(
    username              varchar(255)   not null,
    password              varchar(255)   not null,
    firstname             varchar(255)   not null,
    lastname              varchar(255)   not null,
    SSN                   int            not null,
    dob                   date           not null,
    phone                 varchar(255)   not null,
    email                 varchar(255)   not null,
    addressLine1          varchar(255)   not null,
    addressLine2          varchar(255)   null,
    city                  varchar(255)   not null,
    state                 varchar(255)   not null,
    country               varchar(255)   not null,
    zipcode               varchar(255)   not null,
    maxDistancePreference float          not null,
    latitude              decimal(10, 8) not null,
    longitude             decimal(11, 8) not null,
    groupNumber           int            null,
    constraint SSN_UNIQUE
        unique (SSN),
    constraint username_UNIQUE
        unique (username),
    constraint patients___fk
        foreign key (groupNumber) references prioritygroup (groupNumber)
);

alter table patients
    add primary key (username);

create table providers
(
    username     varchar(255)   not null
        primary key,
    password     varchar(255)   not null,
    name         varchar(255)   not null,
    phone        varchar(255)   not null,
    email        varchar(255)   not null,
    providerType varchar(45)    not null,
    addressLine1 varchar(255)   not null,
    addressLine2 varchar(255)   null,
    city         varchar(255)   not null,
    state        varchar(255)   not null,
    country      varchar(255)   not null,
    zipcode      varchar(255)   not null,
    latitude     decimal(10, 8) not null,
    longitude    decimal(11, 8) not null
);

create table weeklytimeslot
(
    slotid    int  not null
        primary key,
    weekday   int  not null,
    startTime time not null,
    endTime   time not null
);

create table appointment
(
    appointmentid    int          not null
        primary key,
    ProviderUsername varchar(255) not null,
    appointmentDate  datetime     not null,
    slotid           int          not null,
    availableNumber  int          not null,
    constraint provider
        foreign key (ProviderUsername) references providers (username),
    constraint slot
        foreign key (slotid) references weeklytimeslot (slotid)
);

create index provider_idx
    on appointment (ProviderUsername);

create index slot_idx
    on appointment (slotid);

create table offerappointment
(
    appointmentid   int          not null,
    PatientUsername varchar(255) not null,
    status          varchar(255) not null,
    expiretime      datetime     not null,
    primary key (appointmentid, PatientUsername),
    constraint Patient
        foreign key (PatientUsername) references patients (username),
    constraint appointmentId
        foreign key (appointmentid) references appointment (appointmentid)
);

create index PatientUsename_idx
    on offerappointment (PatientUsername);

create table timepreference
(
    patientUsername varchar(255) not null,
    slotid          int          not null,
    primary key (patientUsername, slotid),
    constraint patientUsername
        foreign key (patientUsername) references patients (username),
    constraint slotid
        foreign key (slotid) references weeklytimeslot (slotid)
);

create index slotid_idx
    on timepreference (slotid);

