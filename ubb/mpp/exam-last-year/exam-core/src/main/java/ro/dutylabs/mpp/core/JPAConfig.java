package ro.dutylabs.mpp.core;

import com.google.common.cache.CacheBuilder;
import org.postgresql.ds.PGPoolingDataSource;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.cache.CacheManager;
import org.springframework.cache.annotation.EnableCaching;
import org.springframework.cache.guava.GuavaCacheManager;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.jpa.repository.config.EnableJpaRepositories;
import org.springframework.orm.hibernate4.HibernateExceptionTranslator;
import org.springframework.orm.jpa.JpaTransactionManager;
import org.springframework.orm.jpa.LocalContainerEntityManagerFactoryBean;
import org.springframework.orm.jpa.vendor.Database;
import org.springframework.orm.jpa.vendor.HibernateJpaVendorAdapter;
import org.springframework.transaction.PlatformTransactionManager;
import org.springframework.transaction.annotation.EnableTransactionManagement;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.sql.DataSource;
import java.util.concurrent.TimeUnit;

/**
 * Created by cosmin on 11/06/2017.
 */

@Configuration
@EnableJpaRepositories({"ro.dutylabs.mpp.core.repository"})
@EnableTransactionManagement
@EnableCaching
public class JPAConfig {

//    @Value("${db.jdbcURL}")
//    private String jdbcURL;

    @Value("${db.serverName}")
    private String serverName;

    @Value("${db.databaseName}")
    private String databaseName;

    @Value("${db.user}")
    private String user;

    @Value("${db.password}")
    private String password;

    @Value("${db.generateDDL}")
    private Boolean generateDDL;


    @Bean
    public DataSource dataSource() {
        PGPoolingDataSource dataSource = new PGPoolingDataSource();
        //            dataSource.setUrl(jdbcURL);
        dataSource.setServerName(serverName);
        dataSource.setDatabaseName(databaseName);
        dataSource.setUser(user);
        dataSource.setPassword(password);
        dataSource.setMaxConnections(4);

        return dataSource;
    }

    @Bean
    public EntityManagerFactory entityManagerFactory() {
        HibernateJpaVendorAdapter vendorAdapter = new HibernateJpaVendorAdapter();
        vendorAdapter.setDatabase(Database.POSTGRESQL);
        vendorAdapter.setGenerateDdl(generateDDL);
        vendorAdapter.setShowSql(true);

        LocalContainerEntityManagerFactoryBean factory = new LocalContainerEntityManagerFactoryBean();
        factory.setJpaVendorAdapter(vendorAdapter);
        factory.setPackagesToScan("ro.dutylabs.mpp.core.model");
        factory.setDataSource(dataSource());
        factory.afterPropertiesSet();
        return factory.getObject();
    }

    @Bean
    public EntityManager entityManager() {
        return entityManagerFactory().createEntityManager();
    }

    @Bean
    PlatformTransactionManager transactionManager() {
        JpaTransactionManager manager = new JpaTransactionManager();
        manager.setEntityManagerFactory(entityManagerFactory());
        return manager;
    }

    @Bean
    public HibernateExceptionTranslator hibernateExceptionTranslator() {
        return new HibernateExceptionTranslator();
    }

    @Bean
    public CacheManager cacheManager() {
        GuavaCacheManager guavaCacheManager = new GuavaCacheManager();
        guavaCacheManager.setCacheBuilder(CacheBuilder.newBuilder().expireAfterAccess(2, TimeUnit.HOURS));
        return guavaCacheManager;
    }
}

