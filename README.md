# iot


---

# Design of IoT Service platform for smart home system


## Abstract
With the maturity of technologies such as Internet of Things, big data, cloud computing, the development of Internet of Things applications has been booming. Smart homes, as an important application area of Internet of Things technology, have been widely studied in recent years, and a large number of applications have also emerged product. At present, smart home design mainly exists, lacks theoretical basis, existing system control capability is poor, scalability is insufficient, server resource utilization efficiency is not high, and there are problems such as high access threshold and poor compatibility of the platform.

In view of the above issues, the four-tier architecture of the Internet of Things is proposed, that is, a platform layer is added to the original three-tier architecture of the Internet of Things to connect the technology solutions of the application layer and the perception layer of the Internet of Things, and a set of smart home internet of things service platforms is researched and developed.

This article studies the theory and many technical solutions of smart home systems, and develops a web-based PaaS/IoT PaaS hybrid smart home networking service platform based on RESTful-style services. The smart home service platform adopts Web Service technology to provide web interfaces on the one hand. On the other hand, the MQTT protocol event interface is implemented based on the Web interface. InfluxDB time series storage is adopted for smart home device data, combined with a smart home gateway to achieve concurrent access to massive smart home IoT devices and persistent storage of device data clouds, and remote intelligent control. Other important functions.

After a rigorous software testing process, this smart home IoT service platform can effectively solve many problems in current smart home systems and can provide a safe and reliable service.

## Keywords
Keywords：Smart Home; IoT Platform; MQTT; Web Service; REST

## Architecture
![IoT Architecture](https://github.com/ATM006/iot/blob/origin/dev/docs/image/%E7%B3%BB%E7%BB%9F%E6%95%B4%E4%BD%93%E6%9E%B6%E6%9E%84.png "System overall architecture")

智能家居物联网服务平台软件架构分层设计，包括数据存储系统、数据访问层、接口访问层、设备适配层。智能家居物联网服务平台的体系架构如图所示。

![IoT Platform](https://github.com/ATM006/iot/blob/origin/dev/docs/image/%E5%B9%B3%E5%8F%B0%E6%9E%B6%E6%9E%84.png "The architecture diagram of the Internet of things service platform")

系统体架构构图

数据存储系统，实现设备数据的持久化存储，利用MongoDB数据和InfluxDB实现对数据的持久化存储。

数据访问层位于数据存储系统和接口访问层之间，利用底层数据存储系统的数据服数据访问层层是通过服务接口模块实现的。服务接口模块主要实现系统数据访问层的接口，包括区域、租户、用户、设备和事件的内部接口。这些接口是整个系统服务的核心，负责为下层模块提供数据访问服务。服务接口模块的服务仅供系统内部模块调用。

接口访问层位于数据访问层和设备适配层之间，利用上层数据访问层服务接口模块的服务接口进行数据处理和转发，并对外提供应用程序编程接口。本层由三个模块组成，分别是事件管理模块、MQTT事件模块、综合管理模块。事件管理模块包括对设备数据和用户命令的处理和转发功能；MQTT事件模块订阅MQTT broker的消息根据消息内容调用事件管理模块接口；综合管理模块实现对上层的站点、租户、用户、设备等服务接口的封装对外提供服务。

设备适配层位于接口访问层与智能网关设备之间，利用上层接口为网关设备提供服务。设备接入层主要解决支持不同物联网协议的设备接入问题，本系统以物联网标准协议MQTT协议作为实例进行探索。设备适配层包含一个MQTT broker，该层实现了MQTT协议设备接入智能家居服务平台。


## Interface



